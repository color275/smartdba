
from django import forms
from .models import *
# from django_summernote.widgets import SummernoteWidget
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.db.models import Q

from django.db import connections
from bootstrap_datepicker_plus import DateTimePickerInput

import datetime
import time

################################################
## slack
################################################
import os
from slack import WebClient
from slack.errors import SlackApiError

import requests



iamSql = """select A.emp_no, A.emp_nm, A.sub_mail, A.mobile, c.name
					from iam.EX_GW_EMP_TOTAL A,
					     iam.ORG_USER B,
					     IAM.ORG_GROUP C
					where A.EMP_NO = B.CODE
					  AND B.GROUP_ID = C.GROUP_ID
					  AND EMP_STATUS IN ('H','C')
					  AND SUB_MAIL IS NOT NULL
					  AND A.EMP_NO = '{emp_no}'
				"""


def _query_dict(db_nm, sql):
    """
    Queries mysql and returns a cursor to the results.
    """
    try :
	    with connections[db_nm].cursor() as cur :
	    	cur.execute(sql)

	    	columnNames = [d[0] for d in cur.description]
	    	dataset = [dict(zip(columnNames, row)) for row in cur]

    except :
    	dataset = [{'EMP_NM':'?','NAME':'?','MOBILE':'?','SUB_MAIL':'?'}]

    return dataset

def _send_slack(msg)   :

  client = WebClient(token='xoxp-127066622802-291541382084-705305252917-63304c080942bf49ae37f184eeddb286')

  try:
      response = client.chat_postMessage(
          channel='#gsshop-db',
          text=msg,
          username="SmartDBA",
          icon_emoji=":smartdba2_0:")
  except SlackApiError as e:
      # You will get a SlackApiError if "ok" is False
      print("Got an error: " + e.response['error'])

def _query_sms(tel, msg, email=None):
    try :
        ###############################################################################################

        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer wkftodrlsrpchlrhdi!',
            'Content-Type': 'application/json',
        }

        data = '{"id":"100019968604040","message":"' + "[other] " + msg + '","botType":"SMARTDBA_BOT"}'

        data = data.encode("utf-8")

        response = requests.post('https://tong.gsshop.com/api/msg/send', headers=headers, data=data)

        ###############################################################################################
    	

        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer wkftodrlsrpchlrhdi!',
        }

        params = (
            ('email', email),
        )

        response = requests.get('https://tong.gsshop.com/api/users/findByEmail', headers=headers, params=params)

        _send_slack(msg)

        if response.status_code == 200 :

            workplace_id = response.json()['id']                        

            headers = {
                'accept': 'application/json',
                'Authorization': 'Bearer wkftodrlsrpchlrhdi!',
                'Content-Type': 'application/json',
            }

            data = '{"id":"' + workplace_id + '","message":"' + msg + '","botType":"SMARTDBA_BOT"}'
            
            data = data.encode("utf-8")

            response = requests.post('https://tong.gsshop.com/api/msg/send', headers=headers, data=data)

        else :           
            
            with connections["sms"].cursor() as cur :
            	sql = """insert into LGORA_OWN.SC_TRAN  (TR_NUM,
            												TR_SENDDATE,
            												TR_SENDSTAT,
            												TR_MSGTYPE,
            												TR_PHONE,
            												TR_CALLBACK,
            												TR_MSG,
            												TR_CODE)
            										values (
            										        LGORA_OWN.SC_SEQUENCE.NEXTVAL,
            												sysdate,
            												'0',
            												'0',
            												'{tel}',
            												'0220070910',
            												'{msg}',
            												'008')""".format(tel=tel,
            																 msg=msg)
            	cur.execute(sql)
            	connections["sms"].commit()
    except Exception as e :
        print(e)      

# def _query_sms(tel, msg)	 :

# 	_send_slack(msg)

# 	with connections["sms"].cursor() as cur :

# 		sql = """insert into LGORA_OWN.SC_TRAN  (TR_NUM,
# 													TR_SENDDATE,
# 													TR_SENDSTAT,
# 													TR_MSGTYPE,
# 													TR_PHONE,
# 													TR_CALLBACK,
# 													TR_MSG,
# 													TR_CODE)
# 											values (
# 											        LGORA_OWN.SC_SEQUENCE.NEXTVAL,
# 													sysdate,
# 													'0',
# 													'0',
# 													'{tel}',
# 													'0220070910',
# 													'{msg}',
# 													'008')""".format(tel=tel,
# 																	 msg=msg)
# 		cur.execute(sql)
# 		connections["sms"].commit()


class searchKeywordForm(forms.Form):
    keyword = forms.CharField(min_length=2,
					    	  required=True,
					    	  widget=forms.TextInput(attrs={'placeholder': '궁금한 데이터를 찾아보세요',
					    	  	                            "class":"form-control input-lg",
					    	  	                            "id":"id_keyword",}))




class MonitorForm(forms.Form):



    str_date = forms.DateField(
        widget=DateTimePickerInput(options={"format": "YYYY-MM-DD HH:mm"}))
    end_date = forms.DateField(
        widget=DateTimePickerInput(options={"format": "YYYY-MM-DD HH:mm"}))
    interval = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': '간격(분 단위)','style':"width:180px;height:33px;"}))
    




class MetaForm(forms.Form):

	# 3	WEBDB
	# 10	SMTC
	# 19	통합보험
	# 31	인사
	# 40	방송넷/ODS
	# 39	데이터허브

	sql = """
			select '' k, '== SELECT ==' tablespace_name
			from dual
			union all
			select distinct tablespace_name k, concat(db_use,' : ',tablespace_name) tablespace_name
			from
			(
				select db_use, tablespace_name, id_dblist
				from stg_dba_segments
				where id_dblist in (3,10,19,31,40,39)
				  and owner in (
									'SMTC_OWN'
									,'INSU_OWN'
									,'CPROJECT'
									,'GSHS'
									,'SDHUB_OWN'
									,'MPROJECT'
									,'DHUB_OWN'
									,'STORE_OWN'
									,'WMS_OWN'
									,'WMS_INF'
									,'EHR_GSS'
								)
				  and tablespace_name is not null
				  and tablespace_name <> 'USERS'
				  and segment_type = 'TABLE'
				  order by id_dblist
			) a
	"""
	ds_tab_tbs = _query_dict("default",sql)

	choice_tab_tbs = []
	for tbs in ds_tab_tbs :
		choice_tab_tbs.append([tbs['k'], tbs['tablespace_name']])

	sql = """
			select '' k, '== SELECT ==' tablespace_name
			from dual
			union all
			select distinct tablespace_name k, concat(db_use,' : ',tablespace_name) tablespace_name
			from
			(
				select db_use, tablespace_name, id_dblist
				from stg_dba_segments
				where id_dblist in (3,10,19,31,40,39)
				  and owner in (
									'SMTC_OWN'
									,'INSU_OWN'
									,'CPROJECT'
									,'GSHS'
									,'SDHUB_OWN'
									,'MPROJECT'
									,'DHUB_OWN'
									,'STORE_OWN'
									,'WMS_OWN'
									,'WMS_INF'
									,'EHR_GSS'
								)
				  and tablespace_name is not null
				  and tablespace_name <> 'USERS'
				  and segment_type = 'INDEX'
				  order by id_dblist
			) a
	"""
	ds_ind_tbs = _query_dict("default",sql)

	choice_ind_tbs = []
	for tbs in ds_ind_tbs :
		choice_ind_tbs.append([tbs['k'], tbs['tablespace_name']])


	choice_owner = [    ['','== SELECT =='],
						['SMTC_OWN', 'SMTC : SMTC_OWN'],
						['WMS_OWN','SMTC : WMS_OWN'],
						['WMS_INF','SMTC : WMS_INF'],
						['INSU_OWN','WEBDB : INSU_OWN'],
						['STORE_OWN','WEBDB : STORE_OWN'],
						['CPROJECT','방송넷/ODS : CPROJECT'],
						['MPROJECT','방송넷/ODS : MPROJECT'],
						['GSHS','통합보험 : GSHS'],
						['SDHUB_OWN','데이터허브 : SDHUB_OWN'],
						['DHUB_OWN','데이터허브 : DHUB_OWN'],
						['EHR_GSS','인사 : EHR_GSS'],
				   ]


	choice_init = [('','== SELECT ==')]
	choice_role = [(u[1], u[0] + " : " + u[1]) for u in MetaGrantList.objects.filter().values_list('id_dblist__db_use','app_service').distinct().order_by('id_dblist__db_use')]

	choice_role = choice_init + choice_role






	# filter = TableList.objects.filter( Q(id_dblist__in=[3,10,19,31,40,39]),
	# 								   Q(owner__in=['SMTC_OWN'
	# 												,'INSU_OWN'
	# 												,'CPROJECT'
	# 												,'GSHS'
	# 												,'SDHUB_OWN'
	# 												,'MPROJECT'
	# 												,'DHUB_OWN'
	# 												,'STORE_OWN'
	# 												,'WMS_OWN'
	# 												,'WMS_INF'
	# 												,'EHR_GSS']),
	# 								   ~Q(tablespace_name=None),
	# 								   ~Q(tablespace_name='USERS')

	# 	                              )
	# ds_tbs = filter.values('db_use','tablespace_name').order_by('db_use').distinct()







	choice_tab_tbs = forms.ChoiceField(  required = False,
								  choices=choice_tab_tbs,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:180px;height:29px;font-size: 12px ! important;"}))
	choice_ind_tbs = forms.ChoiceField(  required = False,
								  choices=choice_ind_tbs,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:180px;height:29px;font-size: 12px ! important;"}))
	choice_owner = forms.ChoiceField(  required = False,
								  choices=choice_owner,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:150px;height:29px;font-size: 12px ! important;"}))

	choice_role = forms.ChoiceField(  required = False,
								  choices=choice_role,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:150px;height:29px;font-size: 12px ! important;"}))



class DataSearchForm(forms.ModelForm):

	choice_db_type =   (
					('', '전체 DB'),
					(39, '데이터허브'),
					(10, 'SMTC'),
					(3, 'WEBDB'),
					(40, 'ODS/방송넷'),
				)

	choice_my_data =   (
					('', '전체 데이터'),
					(1, '나의 데이터'),
				)

	db_type = forms.ChoiceField(  required = False,
								  choices=choice_db_type,
								  widget=forms.Select(attrs={"class":"form-control"}))
	my_data = forms.ChoiceField(  required = False,
								  choices=choice_my_data,
								  widget=forms.Select(attrs={"class":"form-control"}))

	class Meta :
		model = DataList
		fields = (
				'data_title',
			)
		widgets = {
			'data_title' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': 'BEST 상품 리스트'},),
		}

class ObjectListForm(forms.ModelForm):

	choice_object_type =   (
							('','오브젝트 전제'),
							('DATABASE LINK','DATABASE LINK'),
							('FUNCTION','FUNCTION'),
							('INDEX','INDEX'),
							# ('INDEX PARTITION','INDEX PARTITION'),
							# ('INDEX SUBPARTITION','INDEX SUBPARTITION'),
							('JOB','JOB'),
							('MATERIALIZED VIEW','MATERIALIZED VIEW'),
							('PACKAGE','PACKAGE'),
							('PACKAGE BODY','PACKAGE BODY'),
							('PROCEDURE','PROCEDURE'),
							('SEQUENCE','SEQUENCE'),
							# ('TABLE','TABLE'),
							# ('TABLE PARTITION','TABLE PARTITION'),
							# ('TABLE SUBPARTITION','TABLE SUBPARTITION'),
							('TRIGGER','TRIGGER'),
							('TYPE','TYPE'),
							('TYPE BODY','TYPE BODY'),
							('VIEW','VIEW'),
						  )

	choice_object_type = forms.ChoiceField(  required = False,
								  choices=choice_object_type,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:150px;height:29px;font-size: 12px ! important;"}))

	owner = forms.ModelChoiceField(required = False,
		                          queryset=DBOwner.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_DBOwner', forward=['id_dblist'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Onwer',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))

	class Meta :
		model = ObjectList
		fields = (
				'object_name',
				'id_dblist',
				'oper_cd'
			)
		widgets = {
			'object_name' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': 'PG_PMO_PRD_PMO'},),
			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList', forward=['oper_cd'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'oper_cd': autocomplete.ModelSelect2(url='Autocomplete_OperCd',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 운영/개발',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}

class GrantListForm(forms.ModelForm):

	class Meta :
		model = GrantList
		fields = (
				'grantee',
				'table_name',
				'id_dblist',
				'oper_cd'
			)
		widgets = {
			'grantee' : forms.TextInput(attrs={'class':'form-control input-lg','style':'width:46%', 'placeholder': 'SMTC_APP (옵션)'},),
			'table_name' : forms.TextInput(attrs={'class':'form-control input-lg', 'style':'width:46%', 'placeholder': 'ORD_ORD_M (필수)'},),
			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList', forward=['oper_cd'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'oper_cd': autocomplete.ModelSelect2(url='Autocomplete_OperCd',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 운영/개발',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}

class StdDomainForm(forms.ModelForm):



  data_type = forms.ModelChoiceField(required=True,
  	                          queryset=StdDataType.objects.all(),
  	                          widget=forms.Select(attrs={"class":"form-control"}))

  leng = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '5',
					    	  	                            "class":"form-control input-sm"}))

  decimal_leng = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '2',
					    	  	                            "class":"form-control input-sm"}))



  class Meta :
    model = StdDomain
    fields = (
        'domain_name',
        'id_std_domaintype',
        'expl',
        'group_code',
        'group_code_yn'
      )
    widgets = {
      'domain_name' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': '예치금'},),
      'group_code' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': '그룹코드명 or 테이블영문명'},),
      'group_code_yn': forms.Select(attrs={"class":"form-control",'style':"height:29px;font-size: 12px ! important;"}),
      # 'oracle_leng' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': '5'},),
      # 'oracle_decimal_leng' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': '2'},),
      'expl' : forms.Textarea(attrs={'class':'form-control input-sm', 'placeholder': '설명'},),
      'id_std_domaintype': autocomplete.ModelSelect2(url='Autocomplete_StdDomainType',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 도메인타입',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
    }

class StdWordForm(forms.ModelForm):

  choice_tab_or_col =   (
              (1, '한글단어명'),
              (2, '영문단어명'),
              (3, '영문FULL명'),
              )

  choice_tab_or_col = forms.ChoiceField(  required = False,
                  choices=choice_tab_or_col,
                  widget=forms.Select(attrs={"class":"form-control",'style':"width:150px;height:29px;font-size: 12px ! important;"}))



  class Meta :
    model = StdWord
    fields = (
        'std_wd_kor',
        'std_wd_eng',
        'std_wd_eng_ful',
        'expl',
      )
    widgets = {
      'std_wd_kor' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': '상품'},),
      'std_wd_eng' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': 'PRD'},),
      'std_wd_eng_ful' : forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': 'PRODUCT'},),
      'expl' : forms.Textarea(attrs={'class':'form-control input-sm', 'placeholder': '장사로 파는 물건 또는 매매를 목적으로..'},),
    }




class ExecuteSQLLV(forms.ModelForm):

	class Meta :
		model = TableList
		fields = (
				'id_dblist',
			)

		widgets = {

			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_ExecuteSQL_DbList',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}

class TableListForm(forms.ModelForm):

	choice_tab_or_col =   (
							(1, 'TABLE'),
							(2, 'COLUMN'),
						  )

	choice_tab_or_col = forms.ChoiceField(  required = False,
								  choices=choice_tab_or_col,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:100px;height:29px;font-size: 12px ! important;"}))

	choice_option =   (
							('', 'Option'),
							('CDC', 'CDC'),
							('개인정보', '개인정보'),
						  )

	choice_option = forms.ChoiceField(  required = False,
								  choices=choice_option,
								  widget=forms.Select(attrs={"class":"form-control",'style':"width:100px;height:29px;font-size: 12px ! important;"}))

	owner = forms.ModelChoiceField(required = False,
		                          queryset=DBOwner.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_DBOwner', forward=['id_dblist'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Onwer',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))


	class Meta :
		model = TableList
		fields = (
				'table_name',
				'id_dblist',
				'oper_cd',
			)
		widgets = {
			'table_name' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': '테이블 영문영 ( keyword% )'},),
			'oper_cd': autocomplete.ModelSelect2(url='Autocomplete_OperCd',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 운영/개발',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList', forward=['oper_cd'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}

class MetaReqForm(forms.ModelForm):




	# str_date = forms.DateField(
 #    widget=DateTimePickerInput(
 #    						   attrs={'class': 'datetimepicker-input form-control input-sm','style': 'width:100%;',
	# 				        	      'value': (WeekDBA.objects.all().first()).dist_dtm}))



	owner = forms.ModelChoiceField(required = False,
		                          queryset=DBOwner.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_DBOwner', forward=['id_dblist'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Onwer 선택',
				                                           'style': 'width:50px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))

	data_tbs = forms.ModelChoiceField(required = False,
		                          queryset=DBTablespace.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_DBTablespace', forward=['owner'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Data Tbs',
				                                           'style': 'width:50px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))

	ind_tbs = forms.ModelChoiceField(required = False,
		                          queryset=DBTablespace.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_DBTablespace', forward=['owner'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Index Tbs',
				                                           'style': 'width:50px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))

	grant = forms.ModelChoiceField(required = False,
		                          queryset=DBTablespace.objects.all(),
								  widget=autocomplete.ModelSelect2(url='Autocomplete_MetaGrantList', forward=['id_dblist'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Grant',
				                                           'style': 'width:50px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },))

	class Meta :





		model = MetaReq
		fields = (
				'id_tablelist',
				'id_dblist',
				'title',
				'csr',
				'req_contents',
				'table_name',
				'table_comments',
				'obj_class',
				'obj_new',
				'storage_cycle',
				'storage_cycle_column',
				'id_domainanddblist',
				'id_pl_dev',
				'dist_dtm',
			)
		widgets = {

			'obj_class': forms.Select(attrs={"class":"form-control",'style':"height:29px;font-size: 12px ! important;"}),
			'obj_new': forms.Select(attrs={"class":"form-control",'style':"height:29px;font-size: 12px ! important;"}),
			'req_contents' : forms.Textarea(attrs={'class':'form-control input-lg', 'placeholder': 
"""* 신규 테이블 : 필요 권한 입력 (ex) JNDI : jdbc/smtcdb, SMTC_BAT : SELECT,INSERT,DELETE,UPDATE, SAS : INSERT,DELETE
* 신규 인덱스 : 튜닝번호 입력 (ex) 튜닝번호 : 1000
* 신규 권한 : 튜닝번호 필수 입력 (ex) 튜닝번호 : 1000
* 권한/프로시져/인덱스 등 SCRIPT 는 아래 박스에서 안내하는 형식에 맞게 넣어주세요""",'style': 'width:100%;','rows':4},),
			'title' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': '(필수) 신청하고자 하는 오브젝트 영문명을 입력하세요','style': 'width:70%'},),
			'csr' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': '(필수) CSR 또는 행봇 번호를 입력하세요','style': 'width:29%'},),
			'table_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': '테이블 영문명','style': 'width:200px;height:28px'},),
			'table_comments' : forms.TextInput(attrs={'class':'form-control', 'placeholder': '테이블 한글명','style': 'width:200px;height:28px'},),
			'storage_cycle' : forms.TextInput(attrs={'type':'number', 'class':'form-control', 'placeholder': '보관주기(월,숫자)','style': 'width:150px;height:28px'},),
			'storage_cycle_column' : forms.TextInput(attrs={'class':'form-control', 'placeholder': '보관주기 - 기준컬럼(REG_DTM)','style': 'width:230px;height:28px'},),

			'dist_dtm' : forms.DateInput(attrs={'class': 'datepicker form-control input-sm','style': 'width:100%;',
										       'value': (WeekDBA.objects.all().first()).dist_dtm}),



			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_MetaReq_DbList',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': '데이터베이스 선택',
				                                           'style': 'width:50px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'id_tablelist': autocomplete.ModelSelect2(url='Autocomplete_TableList_Meta', forward=['id_dblist','owner'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': '테이블 선택',
				                                           'style': 'width:300px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'id_domainanddblist': autocomplete.ModelSelect2(url='Autocomplete_DomainAndDbList', forward=['id_dblist'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': '도메인 선택',
				                                           'style': 'width:200px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'id_pl_dev': autocomplete.ModelSelect2(url='Autocomplete_MetaReq_User_Search',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': '승인자 선택',
				                                           'style': 'width:200px',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}


class CreateDDLLVForm(forms.Form):
    sheet_name = forms.CharField(min_length=2,
					    	  required=False,
					    	  widget=forms.TextInput(attrs={'placeholder': '구글 시트 명 입력',
					    	  	                            "class":"form-control input-lg",
					    	  	                            }))
    


class MetaReqLVForm(forms.ModelForm):

	choice_status =   (
	            ('', '상태 선택'),
	            # (1, '개발 - PL 승인 중'),
	            # (2, '개발 - DA 승인 중'),
	            (3, '개발 반영 예정'),
	            (4, '개발 완료'),
	            (5, 'PL 승인 대기'),
	            (6, '운영 반영 예정'),
	            (7, '운영 완료'),
	            (8, '반려'),
	            )



	choice_status = forms.ChoiceField(  required = False,
	                choices=choice_status,
	                widget=forms.Select(attrs={"class":"form-control",'style':"width:200px;height:29px;font-size: 12px ! important;"}))


	class Meta :
		model = MetaReq
		fields = (
				'title',
			)
		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': '메타번호 or 제목 or 테이블 영문명 or 등록자 검색','style': 'width:100%'},),
		}

class ColumnListForm(forms.ModelForm):


	class Meta :
		model = ColumnList
		fields = (
				'id_tablelist',
				'id_dblist',
				'oper_cd',
			)
		widgets = {
			'id_tablelist': autocomplete.ModelSelect2(url='Autocomplete_TableList',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Table',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'oper_cd': autocomplete.ModelSelect2(url='Autocomplete_OperCd',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 운영/개발',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}



class UserListForm(forms.ModelForm):

	btn_account_active = forms.CharField(required = False)
	class Meta :
		model = UserList
		fields = (
				'username',
				'id_dblist',
				'oper_cd',
			)
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': '이름 Or 계정명으로 조회'}),
			'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList', forward=['oper_cd'],
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select Database',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
			'oper_cd': autocomplete.ModelSelect2(url='Autocomplete_OperCd',
				                                   attrs={
				                                           # Set some placeholder
				                                           'data-placeholder': 'Select 운영/개발',
				                                           # Only trigger autocompletion after 3 characters have been typed
				                                           # 'data-minimum-input-length': 3,
				                                       },),
		}


class TuningListLVForm(forms.ModelForm):

	choice_status =   (
	            ('', '그외 선택'),
	            (1, 'SQL ID 검색'),
	            (2, 'SQL TEXT 검색'),
	            )

	choice_status = forms.ChoiceField(  required = False,
	                choices=choice_status,
	                widget=forms.Select(attrs={"class":"form-control",'style':"width:200px;height:29px;font-size: 12px ! important;"}))

	keyword = forms.CharField(min_length=2,
				    	  required=False,
				    	  widget=forms.TextInput(attrs={'placeholder': '번호 or 제목 or 요청자',
				    	  	                            "class":"form-control input-lg",
				    	  	                            }))

	class Meta:
	    model = TuningList
	    fields = ('id_dblist',
	    		  'id_domain',
	    		  'id_tuningstatus',
	    		  'id_projectlist',
	    		  )
	    widgets = {
	    	'id_tuningstatus': forms.Select(attrs={"class":"form-control",'style':"height:29px;font-size: 12px ! important;"}),

	    	'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList', forward=['oper_cd'],
	    		                                   attrs={
	    		                                           'data-placeholder': '데이터베이스 선택',
	    		                                       },),
	        'id_domain': autocomplete.ModelSelect2(url='Autocomplete_Domain',
				                                   attrs={
				                                           'data-placeholder': '도메인 선택',
				                                           'style':"width:300px",
				                                       },),
	        'id_projectlist': autocomplete.ModelSelect2(url='Autocomplete_ProjectList',
				                                   attrs={
				                                           'data-placeholder': '프로젝트 선택',
				                                           'style':"width:300px",
				                                       },),
	    }

	def __init__(self, *args, **kwargs):
	        super(TuningListLVForm, self).__init__(*args, **kwargs)
	        self.fields['id_tuningstatus'].empty_label = '튜닝상태 선택'


class TuningListDVForm(forms.ModelForm):	

	class Meta:
	    model = TuningList
	    fields = (
	    		  'id_tuningstatus',	    		  
	    		  )
	    widgets = {
	    	'id_tuningstatus': forms.Select(attrs={"class":"form-control",'style':"height:29px;font-size: 12px ! important;"}),

	    }

	# def __init__(self, *args, **kwargs): 
	# 	super(TuningListDVForm, self).__init__(*args, **kwargs) 
	# 	self.fields['id_tuningstatus'].empty_label = '튜닝상태 선택'
	def __init__(self, *args, **kwargs):
	    self.request = kwargs.pop("request", None)	    
	    obj_id = kwargs.pop('obj_id', None)

	    super(TuningListDVForm, self).__init__(*args, **kwargs)
	    
	    self.fields['id_tuningstatus'].empty_label = '튜닝상태 선택'	    
	    self.fields['id_tuningstatus'].initial = (TuningList.objects.get(id=obj_id)).id_tuningstatus.id

	    if self.request.user.is_superuser : 
	    	self.fields['id_tuningstatus'].queryset = TuningStatus.objects.all() 
	    else : 
	    	self.fields['id_tuningstatus'].queryset = TuningStatus.objects.filter(id__in = [1,2,3])





class TuningListForm(forms.ModelForm):

	class Meta:
	    model = TuningList
	    fields = (
	    	# 'id_reg_user',
	    	'id_tuningstatus',
	    	'title',
	    	'sql_id',
	    	'id_dblist',
	    	'id_domain',
	    	'id_projectlist',
	    	'dist_dtm',
	    	'sql_type',
	    	'asis_elapsed_time',
	    	'expect_elapsed_time',
	    	'avg_rows',
	    	'daily_exec_cnt',
	    	'sql_info',
	    	'bind_value',
	    	'asis_sql_text',
	    	'tuning_info',
	    	'asis_plan',
	    	'tobe_plan',
	    	'tobe_sql_text',
	    	)
	    widgets = {
	        # 'asis_sql_text': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
	        # 'tobe_sql_text': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
	        # 'tuning_dtm' : forms.DateInput(attrs={'type':'date'}),
	        'dist_dtm' : forms.DateInput(attrs={'class': 'datepicker',
									        	'value': datetime.datetime.now().strftime("%Y-%m-%d")}),
	        # 'bind_value' : forms.Textarea(attrs={'placeholder': '<table><tr></tr></table>- ord_start_dt : 20200101\n- ord_end_dt : 20200110\n- prd_cd : 12345',
									#         	 'rows':5,
									#         	 }),
	        'sql_id' : forms.TextInput(attrs={'placeholder': 'SQL을 구분할 수 있는 식별키입니다. 반드시 입력해주세요'}),
	        'asis_elapsed_time' : forms.TextInput(attrs={'type':'float', 'placeholder': '현재 응답시간을 입력해주세요(초)'}),
	        'expect_elapsed_time' : forms.TextInput(attrs={'type':'float', 'placeholder': '튜닝 후 기대 응답시간을 입력해주세요(초)'}),
	        'daily_exec_cnt' : forms.TextInput(attrs={'type':'float', 'placeholder': '하루에 수행되는 평균 횟수를 입력해주세요'}),
	        'avg_rows' : forms.TextInput(attrs={'type':'number', 'placeholder': '서비스에서 조회되는 평균 건 수를 적어주세요'}),
	        # 'id_reg_user': autocomplete.ModelSelect2(url='Autocomplete_User_Search'),
	        'id_domain': autocomplete.ModelSelect2(url='Autocomplete_Domain',
				                                   attrs={
				                                           'data-placeholder': '도메인 선택 (필수)',
				                                           'style':"width:400px",
				                                       },),
	        'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList',
				                                   attrs={
				                                           'data-placeholder': '데이터베이스 선택 (필수)',
				                                           'style':"width:400px",
				                                       },),
	        'id_projectlist': autocomplete.ModelSelect2(url='Autocomplete_ProjectList',
				                                   attrs={
				                                           'data-placeholder': '프로젝트 선택',
				                                           'style':"width:400px",
				                                       },),
	    }

	def __init__(self, *args, **kwargs):
	    self.request = kwargs.pop("request", None)

	    super(TuningListForm, self).__init__(*args, **kwargs)

	    if self.request.user.is_superuser :
	    	self.fields['id_tuningstatus'].queryset = TuningStatus.objects.all()
	    else :
	    	self.initial['id_tuningstatus'] = TuningStatus.objects.get(id = 1)
	    	self.fields['id_tuningstatus'].queryset = TuningStatus.objects.filter(id__in = [1])
	    	# print(self.fields['id_tuningstatus'].initial)
	    	# print(self.fields['id_tuningstatus'].queryset)
	    	# self.fields['id_tuningstatus'].initial = (TuningList.objects.get(id=obj_id)).id_tuningstatus.id


	def save(self, commit=True):

		# 1 : 튜닝요청
		# 2 : 튜닝완료/배포요청
		# 3 : 튜닝완료/배포완료
		# 4 : 특이사항 없음
		# 5 : 반려

		# 변경
		if self.instance.id is not None :
		    # DBA
			if self.request.user.is_superuser :
				if self.instance.id_tuningstatus.id in [2,3,4,5] :
					self.instance.tuning_dtm = datetime.datetime.now()
					self.instance.id_tuning_user = self.request.user

					# 2 : 튜닝완료/배포요청
					if self.instance.id_tuningstatus.id == 2 :
						sabun = self.instance.id_reg_user.username

						ds_emp = _query_dict('iam',iamSql.format(emp_no=sabun))[0]
						msg = "[SmartDBA] 튜닝완료(번호 {no}), 배포 진행해주세요".format(no=self.instance.id)
						_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])



				elif self.instance.id_tuningstatus.id in [1] :
					self.instance.tuning_dtm = None
					self.instance.id_tuning_user = None
			# 일반
			else :
			    self.instance.id_mod_user = self.request.user
			    self.instance.mod_dtm = datetime.datetime.now()

		# 신규
		else :
			# DBA
			if self.request.user.is_superuser :
				self.instance.id_reg_user = self.request.user
				self.instance.reg_dtm = datetime.datetime.now()

				if self.instance.id_tuningstatus in [2,3,4,5] :
					self.instance.tuning_dtm = datetime.datetime.now()
					self.instance.id_tuning_user = self.request.user
			# 일반
			else :
			    self.instance.id_reg_user = self.request.user
			    self.instance.reg_dtm = datetime.datetime.now()

		return super(TuningListForm, self).save(commit=True)

class DataListForm(forms.ModelForm):


	class Meta:
	    model = DataList
	    fields = (
	    	'id_dblist',
	    	'privacy_yn',
	    	'realoretl',
	    	'id_domain',
	    	'data_title',
	    	'data_explain',
	    	'sql_text',
	    	'id_req_users',
	    	'id_mod_psbl_users',
	    	'exp_yn',
	    	)
	    widgets = {
	        # 'data_explain': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
	        'id_req_users': autocomplete.ModelSelect2Multiple(url='Autocomplete_User_Search'),
	        'id_mod_psbl_users': autocomplete.ModelSelect2Multiple(url='Autocomplete_User_Search'),
	        'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList_Part'),
	    }

	def __init__(self, *args, **kwargs):
	    self.request = kwargs.pop("request", None)

	    super(DataListForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):

		if self.instance.id is not None :
		    self.instance.id_mod_user = self.request.user
		    self.instance.mod_dtm = datetime.datetime.now()
		else :
		    self.instance.id_reg_user = self.request.user
		    self.instance.id_mod_user = self.request.user
		    self.instance.mod_dtm = datetime.datetime.now()

		if self.instance.privacy_yn == "0" :
			self.instance.prov_yn1 = "1"

		return super(DataListForm, self).save(commit=True)



class DataListUpdateView_Approve_Form(forms.ModelForm):

	class Meta:
	    model = DataList
	    fields = (
	    	'prov_yn1',
	    	'prov_yn1_text',
	    	'prov_yn2',
	    	'prov_yn2_text',
	    	'id_dblist',
	    	'privacy_yn',
	    	'realoretl',
	    	'data_title',
	    	'data_explain',
	    	'sql_text',
	    	'id_req_users',
	    	'id_mod_psbl_users',
	    	'exp_yn',
	    	)
	    widgets = {
	        # 'data_explain': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
	        'id_req_users': autocomplete.ModelSelect2Multiple(url='Autocomplete_User_Search'),
	        'id_mod_psbl_users': autocomplete.ModelSelect2Multiple(url='Autocomplete_User_Search'),
	        'id_dblist': autocomplete.ModelSelect2(url='Autocomplete_DbList_Part'),
	    }

	def __init__(self, *args, **kwargs):
	    self.request = kwargs.pop("request", None)

	    super(DataListUpdateView_Approve_Form, self).__init__(*args, **kwargs)

	def save(self, commit=True):

		if self.instance.id is not None :
		    self.instance.id_mod_user = self.request.user
		else :
		    self.instance.id_reg_user = self.request.user
		    self.instance.id_mod_user = self.request.user

		if self.instance.privacy_yn == "0" :
			self.instance.prov_yn1 = "1"

		return super(DataListUpdateView_Approve_Form, self).save(commit=True)


class DataRequestForm(forms.ModelForm):


	class Meta:
	    model = DataRequest
	    fields = (
	    	'data_title',
	    	'id_datalist',
	    	'data_explain',
	    	'prov_yn',
	    	)
	    widgets = {
	    	'data_title': forms.TextInput(attrs={'style':"width:500px"}),
	        'id_datalist': autocomplete.ModelSelect2(
	        	                                     url='Autocomplete_DataList',
				                                     attrs={
				                                           'data-placeholder': '조회가 필요한 데이터 선택',
				                                           'style':"width:500px",
				                                       },),
	        'prov_yn': forms.Select(attrs={'style':"width:500px"}),
	    }

	def _query_dict(db_nm, sql):
	    """
	    Queries mysql and returns a cursor to the results.
	    """
	    try :
		    with connections[db_nm].cursor() as cur :
		    	cur.execute(sql)

		    	columnNames = [d[0] for d in cur.description]
		    	dataset = [dict(zip(columnNames, row)) for row in cur]

	    except :
	    	dataset = [{'EMP_NM':'?','NAME':'?','MOBILE':'?','SUB_MAIL':'?'}]

	    return dataset

	def __init__(self, *args, **kwargs):
	    self.request = kwargs.pop("request", None)

	    super(DataRequestForm, self).__init__(*args, **kwargs)
	    if self.instance.id is  None :
		    self.fields['data_title'].initial= "데이터 요청합니다"
		    # self.fields['id_datalist'].queryset = DataList.objects.filter(id_req_users=self.request.user.id)
		    self.fields['id_datalist'].help_text = "개인정보가 포함된 데이터만 표시합니다."


	def save(self, commit=True):


		# 변경
		if self.instance.id is not None :

		    self.instance.id_mod_user = self.request.user
		    self.instance.mod_dtm = datetime.datetime.now()

		    # 변경 되었고
		    # 데이터가 선택되어 있으며,
		    # 등록자가 다시 변경했을 때
		    # 승인 대기 상태로 변경, 조회 가능 시간도 NULL 로 변경
		    if self.instance.id_datalist is not None and self.request.user == self.instance.id_reg_user :

		    	self.instance.prov_yn = '0'
		    	self.instance.poss_view_dtm = None

		    	# SMS 발송
		    	ds_emp = _query_dict('iam',iamSql.format(emp_no=self.request.user.username))[0]
		    	msg = """[SmartDBA] 데이터 조회 권한을 요청하였습니다. {title}""".format(title=self.instance.id_datalist.data_title[0:10]+'...')
		    	_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])

		    	ds_emp = _query_dict('iam',iamSql.format(emp_no="22980"))[0]
		    	msg = """[SmartDBA] 데이터 조회 권한이 요청되었습니다. {name}/{team} {title}""".format(name=self.request.user.first_name,
		    																					    team=self.request.user.last_name,
		    																					    title=self.instance.id_datalist.data_title[0:10]+'...')
		    	_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])


		    # 검토여부 상태를 "승인" 으로 선택했고
		    # 변경자가 검토자 일 경우 동작
		    # if self.instance.prov_yn == '1' and self.request.user == self.instance.id_prov_user :
		    if self.instance.id_datalist is not None and self.instance.prov_yn == '1' :
		    	self.instance.prov_yn_dtm = datetime.datetime.now()
		    	self.instance.id_prov_user = self.request.user

		    	dt = datetime.datetime.now() + datetime.timedelta(days=31)
		    	dt = dt.replace(hour=23, minute=59, second=59)
		    	self.instance.poss_view_dtm = dt

		    	## SMS 발송
		    	ds_emp = _query_dict('iam',iamSql.format(emp_no=self.instance.id_reg_user.username))[0]
		    	msg = """[SmartDBA] 데이터 요청이 승인 되었습니다. {dt}까지 확인가능합니다 {title}""".format(dt=dt.strftime("%Y/%m/%d"),
		    																							 title=self.instance.id_datalist.data_title[0:10]+'...')
		    	_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])

		    if self.instance.id_datalist is None and self.request.user == self.instance.id_reg_user :

		    	self.instance.prov_yn = '0'
		    	self.instance.id_prov_user = None


		    # if self.instance.id_datalist is None and self.instance.prov_yn == '1' :
		    # 	self.instance.prov_yn_dtm = datetime.datetime.now()
		    # 	self.instance.id_prov_user = self.request.user
		    	# dt = datetime.datetime.now() + datetime.timedelta(days=1)
		    	# dt = dt.replace(hour=23, minute=59, second=59)
		    	# self.instance.poss_view_dtm = dt

		    	## SMS 발송
		    	# ds_emp = _query_dict('iam',iamSql.format(emp_no=self.instance.id_reg_user.username))[0]
		    	# msg = """[데이터포탈] 데이터 요청 확인이 되었습니다. {dt}까지 확인가능합니다""".format(dt=dt.strftime("%Y/%m/%d"))
		    	# _query_sms(ds_emp['MOBILE'],msg)

		# 신규
		else :
		    self.instance.id_reg_user = self.request.user
		    self.instance.id_mod_user = self.request.user

		    # 신규 등록
		    # 데이터 선택
		    # 승인 상태가 "대기"
		    # if self.instance.id_datalist is not None and self.instance.prov_yn == '0' :
		    if self.instance.id_datalist is not None :

		    	# self.instance.id_prov_user = User.objects.get(pk= DomainAndDbList.objects.filter(Q(id_domain=self.instance.id_datalist.id_domain),
		    	# 															Q(id_dblist=self.instance.id_datalist.id_dblist)).values_list('it_manager', flat=True)[0])

		    	# SMS 발송
		    	ds_emp = _query_dict('iam',iamSql.format(emp_no=self.request.user.username))[0]
		    	msg = """[SmartDBA] 데이터 조회 권한을 요청하였습니다. {title}""".format(title=self.instance.id_datalist.data_title[0:10]+'...')
		    	_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])

		    	ds_emp = _query_dict('iam',iamSql.format(emp_no='22980'))[0]
		    	msg = """[SmartDBA] 데이터 조회 권한이 요청되었습니다. {name}/{team} {title}""".format(name=self.request.user.first_name,
		    																					    team=self.request.user.last_name,
		    																					    title=self.instance.id_datalist.data_title[0:10]+'...')
		    	_query_sms(ds_emp['MOBILE'],msg, email=ds_emp['SUB_MAIL'])

		return super(DataRequestForm, self).save(commit=True)

