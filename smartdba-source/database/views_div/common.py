# # -*-coding: utf-8-*-
# ########################################
# import datetime
# import json
# import logging.config
# import os
# import re
# import time
# import urllib
# from collections import defaultdict
# from decimal import *
# from itertools import chain
# from operator import itemgetter
# ###################################################################
# from pprint import pprint
# ###################################################################
# from django import template
# from django.conf import settings
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.db import connections
# from django.db.models import Avg, Count, Max, Q
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.shortcuts import get_object_or_404, redirect, render
# from django.templatetags.static import static
# from django.urls import reverse_lazy
# from django.views.generic import (
#     CreateView, DeleteView, DetailView, ListView, UpdateView)
# from django.views.generic.edit import FormMixin
# ###################################################################
# import cx_Oracle
# ###################################################################
# from slack import WebClient
# from slack.errors import SlackApiError
# ###################################################################
# from database.forms import *
# from database.models import *
# ###################################################################


# from django.conf import settings
# div_dp = settings.DIV_DP


# def json_default(value):
#   if isinstance(value, datetime.date):
#     return value.strftime('%Y-%m-%d')

# def orderedSet(list):
#     my_set = set()
#     res = []
#     for e in list:
#         if e not in my_set:
#             res.append(e)
#             my_set.add(e)

#     return res

# def test(msg) :
#   print(msg)

# def loggingVisit(request, menu_cd) :
#   new_uservisit = UserVisit(
#         name = request.user.first_name,
#         sabun = request.user.username,
#         team_name = request.user.last_name,
#         id_menulist = MenuList.objects.get(id=menu_cd),
#         reg_dtm = datetime.datetime.now(),
#   )

#   new_uservisit.save()

# def send_slack(msg)   :
#   """Slack 메시지를 전송한다

#   Args:
#       msg (string): 메시지
#   """
#   if div_dp == 'DEV' :
#   	print("########################################")
#   	print("## 개발 MSG")
#   	print("_send_slack")
#   	print("########################################")
#   	print(msg)
  	
#   else :
# 	  client = WebClient(token='xoxp-127066622802-291541382084-705305252917-63304c080942bf49ae37f184eeddb286')

# 	  try:
# 	      response = client.chat_postMessage(
# 	          channel='#gsshop-db',
# 	          text=msg,
# 	          username="SmartDBA",
# 	          icon_emoji=":smartdba2_0:")
# 	  except SlackApiError as e:
# 	      # You will get a SlackApiError if "ok" is False
# 	      print("Got an error: " + e.response['error'])


# def query_sms(tel, msg, slack_yn='Y', sms_yn='Y')   :

# 	if div_dp == 'DEV' :
# 		print("########################################")
# 		print("## 개발 MSG")
# 		print("query_sms")
# 		print("########################################")
# 		print(msg)

# 	else :

# 		if slack_yn == 'Y' :
# 			send_slack(msg)  

# 		if sms_yn == 'Y' :
# 			with connections["sms"].cursor() as cur :

# 			  sql = """insert into LGORA_OWN.SC_TRAN  (TR_NUM,
# 			                        TR_SENDDATE,
# 			                        TR_SENDSTAT,
# 			                        TR_MSGTYPE,
# 			                        TR_PHONE,
# 			                        TR_CALLBACK,
# 			                        TR_MSG,
# 			                        TR_CODE)
# 			                    values (
# 			                            LGORA_OWN.SC_SEQUENCE.NEXTVAL,
# 			                        sysdate,
# 			                        '0',
# 			                        '0',
# 			                        '{tel}',
# 			                        '0220070910',
# 			                        '{msg}',
# 			                        '008')""".format(tel=tel,
# 			                                msg=msg)
# 			  cur.execute(sql)
# 			  connections["sms"].commit()




# def query_dict(db_nm, sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     try :
#       with connections[db_nm].cursor() as cur :
#         cur.execute(sql)

#         columnNames = [d[0] for d in cur.description]
#         dataset = [dict(zip(columnNames, row)) for row in cur]

#     except :
#       # dataset = [{'EMP_NM':'?','NAME':'?','MOBILE':'?','SUB_MAIL':'?'}]
#       dataset = []

#     return dataset

# def query_list(db_nm, sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections[db_nm].cursor() as cur :
#       cur.execute(sql)
#       dataset = cur.fetchall()

#     return dataset

# def query_commit(db_nm, sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections[db_nm].cursor() as cur :
#       cur.execute(sql)
#       connections[db_nm].commit()

#       return 1

# def query_column_name(db_nm, sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections[db_nm].cursor() as cur :
#       cur.execute(sql)

#       columnNames = [d[0] for d in cur.description]

#     return columnNames


# def query_mysql_dict(sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections['default'].cursor() as cur :
#       cur.execute(sql)

#       columnNames = [d[0] for d in cur.description]
#       dataset = [dict(zip(columnNames, row)) for row in cur]

#     return dataset

# def query_mysql_list(sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections['default'].cursor() as cur :
#       cur.execute(sql)
#       dataset = cur.fetchall()

#     return dataset

# def query_mssql_list(sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections['homenet'].cursor() as cur :
#       cur.execute(sql)
#       dataset = cur.fetchall()

#     return dataset

# def query_mssql_dict(sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     try :
#       with connections['homenet'].cursor() as cur :
#         cur.execute(sql)

#         columnNames = [d[0] for d in cur.description]
#         dataset = [dict(zip(columnNames, row)) for row in cur]
#     except :
#       dataset = ""

#     return dataset




# def commit_mysql(sql):
#     """
#     Queries mysql and returns a cursor to the results.
#     """
#     with connections['default'].cursor() as cur :
#       cur.execute(sql)
#       connections['default'].commit()

#       return cur.lastrowid

# def dashboard_data(request) :

#   sql = """
#     select count(distinct sabun) cnt, count(*) total_cnt
#     from cust_user_visit a
#     where reg_dtm >= DATE(SYSDATE())
#       AND reg_dtm < DATE_ADD(DATE(SYSDATE()), INTERVAL 1 DAY)
#   """

#   today_visit = query_mysql_dict(sql)




#   sql = """
#     select id
#     from cust_menu_list
#   """


#   user_permission_all_list = query_list("default",sql)
#   user_permission_all = []
#   for item in user_permission_all_list :
#     user_permission_all.append(item[0])

#   sql = """
#     select id_menulist
#     from cust_menu_permission
#     where id_grantee_user = {user_id}
#   """.format(user_id=request.user.id)



#   user_permission_list = query_list("default",sql)
#   user_permission = []
#   for item in user_permission_list :
#     user_permission.append(item[0])

#   user_permission_minus = list(set(user_permission_all) - set(user_permission))

#   # curr_path = "http://"+request.META['HTTP_HOST']
#   # request.get_full_path()






#   dashboard_context = {
#              'today_visit':today_visit,
#              'user_permission':user_permission,
#              'user_permission_minus':user_permission_minus,

#              }


#   return dashboard_context

# # emp_no, emp_nm, sub_mail, mobile, name
# iamSql = """select A.emp_no, A.emp_nm, A.sub_mail, A.mobile, c.name
#       from iam.EX_GW_EMP_TOTAL A,
#            iam.ORG_USER B,
#            IAM.ORG_GROUP C
#       where A.EMP_NO = B.CODE
#         AND B.GROUP_ID = C.GROUP_ID
#         AND EMP_STATUS IN ('H','C')
#         AND SUB_MAIL IS NOT NULL
#         AND A.EMP_NO = '{emp_no}'
#     """    

# def f_get_datatype( id_stdattr , db_type ) :

#   data = StdAttr.objects.get(id=id_stdattr)

#   in_data_type = ""

#   if data :

#     if db_type == "ORACLE" :
#       in_data_type = data.id_stddomain.oracle_datatype


#     elif db_type in ("MYSQL","MARIADB") :
#       in_data_type = data.id_stddomain.mysql_datatype

#   return in_data_type

# def f_div_attr(attr) :


#   list_attr = [] 

#   if ',' in attr :
#     attr = attr.replace(' ','')
#     list_attr = attr.split(',')
#   elif ' ' in attr :
#     list_attr = attr.split()
#   else :
#     attr = attr.replace(' ','')
#     list_attr = attr.split(',')



#   l_lkor = []
#   l_leng = []
#   l_lcnt = [] 
#   l_domain = []
#   l_eng_attr_name = []
#   l_domain_flag = []
#   l_oracle_domain_datatype = []
#   l_mysql_domain_datatype = []
#   l_word_find_flag = []
#   l_last_num_flag = []
#   l_attr_find = []
#   l_aleary_req = []


#   total_attr = len(list_attr)

#   for attr in list_attr :


#     # print("111")

#     clean_attr = (attr.replace('[','')).replace(']','')
#     attr_exists = StdAttr.objects.filter(std_attr_kor=clean_attr, accept_yn__in=[0,], use_yn=1)

#     if len(attr_exists) > 0 :
#       if attr_exists[0].accept_yn == 1 :
#         l_attr_find.append(False)
#         l_aleary_req.append(True)
#       elif attr_exists[0].accept_yn == 0 :
#         l_attr_find.append(True)
#         l_aleary_req.append(False)

#     else :
#       l_attr_find.append(False)
#       l_aleary_req.append(False)




#     lcnt = []
#     leng = []
#     lkor = []
#     cnt = 1
#     lAtEnNm = ""
#     lAtKrNm = ""
#     word_find_flag = True
#     last_num_flag = True

#     last_number = ""


#     # 공백제거
#     linput = attr.replace(' ','')

#     try :
#       last_number = re.search("([a-zA-Z_가-힣])(\d+$)",linput).group(2)
#       if(len(last_number) > 2) :
#         last_num_flag = False

#       if(int(last_number) > 20) :
#         last_num_flag = False
#     except :
#       pass

#     linput = linput.replace(last_number,'')

#     menual_div = re.findall(r"\[([A-Za-z0-9_가-힣]+)\]", linput)
    

#     # print("222")
#     if menual_div :

#       for data in menual_div :

#         lWdKrNm = data
#         lFindWD = False


#         flag = StdWord.objects.filter(std_wd_kor=data).exists()


#         if flag :
#             std_wd_eng = (StdWord.objects.filter(std_wd_kor=data,accept_yn='0').values('std_wd_eng').first())['std_wd_eng']

#             lAtEnNm = std_wd_eng + "_" + lAtEnNm
#             lAtKrNm = lWdKrNm + "+" + lAtKrNm
#             lkor.append(lWdKrNm)
#             leng.append(std_wd_eng)
#             lcnt.append(cnt)
#             cnt = cnt + 1

#             lFindWD = True

#         if lFindWD == False :

#           word_find_flag = False

#           if len(lkor) > 0 :
#             if lkor[len(lkor)-1:][0] != "<font color='red'>*</font>" :
#               lkor.append("<font color='red'>*</font>")
#               lcnt.append(cnt)
#               cnt = cnt + 1

#             if leng[len(leng)-1:][0] != "<font color='red'>*</font>" :
#               leng.append("<font color='red'>*</font>")
#           else :
#               lkor.append("<font color='red'>*</font>")
#               leng.append("<font color='red'>*</font>")
#               lcnt.append(cnt)
#               cnt = cnt + 1

#     else :

#       lTotalLength = len(linput)

#       while lTotalLength > 0 :

#         i = 1
#         lFindWD = False

#         while i <= lTotalLength :
#           ch = linput[i-1 : ]
#           lWdKrNm = ch




#           flag = StdWord.objects.filter(std_wd_kor=lWdKrNm, accept_yn='0').exists()




#           if flag :
#             std_wd_eng = (StdWord.objects.filter(std_wd_kor=lWdKrNm, accept_yn='0').values('std_wd_eng').first())['std_wd_eng']

#             lAtEnNm = std_wd_eng + "_" + lAtEnNm
#             lAtKrNm = lWdKrNm + "+" + lAtKrNm
#             lkor.append(lWdKrNm)
#             leng.append(std_wd_eng)
#             lcnt.append(cnt)
#             cnt = cnt + 1


#             # 종료 조건
#             lTotalLength = i - 1

#             lFindWD = True


#           i = i + 1

#         lTotalLength = i - 1 - 1
#         linput = linput[0:lTotalLength]




#         if lFindWD == False :

#           word_find_flag = False


#           if len(lkor) > 0 :
#             if lkor[len(lkor)-1:][0] != "<font color='red'>*</font>" :
#               lkor.append("<font color='red'>*</font>")
#               lcnt.append(cnt)
#               cnt = cnt + 1

#             if leng[len(leng)-1:][0] != "<font color='red'>*</font>" :
#               leng.append("<font color='red'>*</font>")
#           else :
#               lkor.append("<font color='red'>*</font>")
#               leng.append("<font color='red'>*</font>")
#               lcnt.append(cnt)
#               cnt = cnt + 1

#       lkor.reverse()
#       leng.reverse()

#     eng_attr_name = '_'.join(leng)
#     eng_attr_name = eng_attr_name + last_number







#     d_ind = 0
#     d_total_length = len(lkor)
#     d_str = ""
#     domain = ""
#     domain_flag = False

#     while d_ind < d_total_length :

#       d_str = ''.join(lkor[d_ind:])



#       if  StdDomain.objects.filter(domain_name=d_str, accept_yn=0, use_yn=1).exists() :


#         domain_flag = True


#       else :
#         sql = """SELECT DOMAIN
#                  FROM CUST_ASIS_ATTR_DOMAIN_MAPPING
#                  WHERE ATTR = '{attr}'
#               """.format(attr=attr)

#         result_ds = query_list("default", sql)

#         if result_ds :
#           d_str = result_ds[0][0]
#           domain_flag = True


#       if domain_flag :
#         domain = StdDomain.objects.filter(domain_name=d_str, accept_yn=0, use_yn=1)
        
#         break
#       d_ind = d_ind + 1


#     # oracle_domain_datatype = []

#     # for d in domain :

#     #   str_oracle_leng = ""

#     #   if d.oracle_decimal_leng != None :
#     #     str_oracle_leng = "(" + str(d.oracle_leng) + ',' + str(d.oracle_decimal_leng) + ")"
#     #   elif d.oracle_leng != None :
#     #     str_oracle_leng = "(" + str(d.oracle_leng) + ")"

#     #   if d.oracle_leng != None :

#     #     # oracle_domain_datatype = d.oracle_data_type + str_oracle_leng + "<br>" + oracle_domain_datatype
#     #     oracle_domain_datatype.append(d.oracle_data_type + str_oracle_leng)


#     #   elif d.oracle_data_type != None :

#     #     oracle_domain_datatype.append(d.oracle_data_type)



#     # mysql_domain_datatype = []
#     l_domain_local = []

#     for d in domain :

#       # str_mysql_leng = ""

#       # if d.mysql_decimal_leng != None :
#       #   str_mysql_leng = "(" + str(d.mysql_leng) + ',' + str(d.mysql_decimal_leng) + ")"
#       # elif d.mysql_leng != None :
#       #   str_mysql_leng = "(" + str(d.mysql_leng) + ")"

#       # if d.mysql_leng != None :
#       #   mysql_domain_datatype.append(d.mysql_data_type + str_mysql_leng)
#       # elif d.mysql_data_type != None :
#       #   mysql_domain_datatype.append(d.mysql_data_type)

#       sql = """select count(*) CNT
#                from cust_std_attr
#                where id_stddomain = {id};
#             """.format(id=d.id)

#       cnt_ds = query_dict("default", sql)

      

#       l_domain_local.append([d.id,d.info_type,cnt_ds[0]['CNT'],d.domain_name])

#     l_lkor.append(lkor)
#     l_leng.append(leng)
#     l_lcnt.append(lcnt)

#     l_eng_attr_name.append(eng_attr_name)
#     l_domain_flag.append(domain_flag)



#     l_domain_local = sorted(l_domain_local, key=itemgetter(2), reverse=True)

#     if attr[-2:] in ('코드','번호') :
#       if len(l_domain_local) > 0 :
#         l_domain_local = [l_domain_local[0]]



#     l_domain.append(l_domain_local)
#     # l_oracle_domain_datatype.append(oracle_domain_datatype)
#     # l_mysql_domain_datatype.append(mysql_domain_datatype)
#     l_word_find_flag.append(word_find_flag)
#     l_last_num_flag.append(last_num_flag)




#   max_length = 0

#   lcnt_ind = 0
#   i = 0
#   for lcnt in l_lcnt :
#     if max_length <= len(lcnt) :
#       max_length = len(lcnt)
#       lcnt_ind = i
#     i = i + 1

#   lcnt = l_lcnt[lcnt_ind]

#   # [, ] 제거

#   buffer_attr = []
#   for attr in list_attr :
#     attr = attr.replace('[','')
#     attr = attr.replace(']','')
#     buffer_attr.append(attr)
#   list_attr = buffer_attr

#   # return  l_lkor, \
#   #         l_leng, \
#   #         l_domain, \
#   #         l_eng_attr_name, \
#   #         l_domain_flag, \
#   #         l_oracle_domain_datatype, \
#   #         l_mysql_domain_datatype, \
#   #         l_word_find_flag, \
#   #         l_last_num_flag, \
#   #         lcnt, \
#   #         total_attr, \
#   #         max_length, \
#   #         l_attr_find, \
#   #         l_aleary_req, \
#   #         list_attr

#   return  l_lkor, \
#           l_leng, \
#           l_domain, \
#           l_eng_attr_name, \
#           l_domain_flag, \
#           l_word_find_flag, \
#           l_last_num_flag, \
#           lcnt, \
#           total_attr, \
#           max_length, \
#           l_attr_find, \
#           l_aleary_req, \
#           list_attr    