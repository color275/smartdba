from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.files.base import ContentFile

import re
import datetime

from django.db.models import Q

from django.conf import settings
from django_safe_fields.fields import SafeCharField
from django_safe_fields.fields import SafeGenericIPAddressField
from django_safe_fields.fields import SafeIntegerField
from fastutils.cipherutils import S12Cipher
from fastutils.cipherutils import AesCipher
from fastutils.cipherutils import MysqlAesCipher
from fastutils.cipherutils import HexlifyEncoder
from fastutils.cipherutils import Utf8Encoder 
from fastutils.cipherutils import mysql_aes_key 
from django.utils.encoding import force_bytes, force_str

# Create your models here.

def get_first_name(self):
    return self.first_name + "(" + self.last_name + ")"

def validate_file_extension(value):
        import os
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.html']
        if not ext.lower() in valid_extensions:
            raise ValidationError('*.html 파일만 업로드 가능합니다')    

User.add_to_class("__str__", get_first_name)

class StdWord(models.Model):

	choice_yn = ( ('1','대기중'),('0','승인'),('2','반려'))
	std_wd_kor = models.CharField('한글단어명',max_length=100, null=True, blank=True)
	std_wd_eng = models.CharField('영문단어명',max_length=100, null=True, blank=True)
	std_wd_eng_ful = models.CharField('영문FULL명',max_length=100, null=True, blank=True)
	accept_yn = models.CharField('승인여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.DO_NOTHING, db_column='id_reg_user', blank=True)
	expl = models.TextField('설명', null=True, blank=True)
	reject_exp = models.TextField('반려사유', null=True, blank=True)

	class Meta :
		verbose_name = '표준단어'
		verbose_name_plural = '표준단어'
		db_table = 'cust_std_word'
	def __str__(self) :
		return self.std_wd_kor

class StdDataType(models.Model):

    data_typ_nm = models.CharField('데이터타입명',max_length=100, null=True, blank=True)

    class Meta :
    	verbose_name = '데이터타입'
    	verbose_name_plural = '데이터타입'
    	db_table = 'cust_std_data_type'
    def __str__(self) :
    	return self.data_typ_nm



class StdDomainType(models.Model):

    domain_type = models.CharField('도메인타입',max_length=100, null=True, blank=True)

    class Meta :
    	verbose_name = '도메인타입'
    	verbose_name_plural = '도메인타입'
    	db_table = 'cust_std_domain_type'
    def __str__(self) :
    	return self.domain_type

class StdDomain(models.Model):

    choice_yn = ( ('1','대기중'),('0','승인'),('2','반려'))
    use_yn = ( ('1','사용'),('0','미사용') )
    group_code_yn = ( ('0','그룹코드(공통코드테이블)'),('1','개별코드(별도테이블)') )

    id_stddatatype = models.ForeignKey(StdDataType, verbose_name='데이터타입명', on_delete=models.PROTECT, db_column='id_stddatatype', blank=True, null=True)
    id_std_domaintype = models.ForeignKey(StdDomainType, verbose_name='도메인타입', on_delete=models.PROTECT, db_column='id_std_domaintype', blank=True, null=True)
    domain_name = models.CharField('도메인명',max_length=100, null=True, blank=True)
    info_type = models.CharField('인포타입',max_length=100, null=True, blank=True)
    oracle_datatype = models.CharField('ORACLE데이터타입',max_length=100, null=True, blank=True)
    mysql_datatype = models.CharField('MYSQL데이터타입',max_length=100, null=True, blank=True)
    expl = models.TextField('설명', null=True, blank=True)
    accept_yn = models.CharField('승인여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
    reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
    id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.DO_NOTHING, db_column='id_reg_user', blank=True)    
    reject_exp = models.TextField('반려사유', null=True, blank=True)
    use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=use_yn, default='1')
    group_code_yn = models.CharField('코드유형', null=True, blank=True, max_length=30, choices=group_code_yn)
    group_code = models.CharField('값(그룹코드 or 테이블영문명)',max_length=100, null=True, blank=True)
    mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)

    # oracle_data_type = models.CharField('데이터타입',max_length=100, null=True, blank=True)
    # oracle_leng = models.IntegerField('데이터길이',null=True, blank=True)
    # oracle_decimal_leng = models.IntegerField('데이터길이',null=True, blank=True)
    # mysql_data_type = models.CharField('데이터타입',max_length=100, null=True, blank=True)
    # mysql_leng = models.IntegerField('데이터길이',null=True, blank=True)
    # mysql_decimal_leng = models.IntegerField('데이터길이',null=True, blank=True)


    class Meta :
    	verbose_name = '표준도메인'
    	verbose_name_plural = '표준도메인'
    	db_table = 'cust_std_domain'
    	ordering = ['info_type']
    def __str__(self) :
    	return self.info_type






class SabunDBUserMapping(models.Model):
    id_userlist = models.OneToOneField(User, on_delete=models.CASCADE, db_column='id_userlist')
    db_username = models.CharField('DB명',max_length=100, default='')

    class Meta :
    	verbose_name = 'DB USER 매핑'
    	verbose_name_plural = 'DB USER 매핑'
    	db_table = 'cust_sabun_dbuser_mapping'
    def __str__(self) :
    	return self.db_username




class OperCd(models.Model) :
	oper_cd = models.CharField('운영구분',max_length=100, default='')

	class Meta :
		verbose_name = '운영구분 (운영/개발/....)'
		verbose_name_plural = '운영구분 (운영/개발/....)'
		db_table = 'cust_oper_cd'

	def __str__(self) :
		return self.oper_cd

class AirflowDagManage(models.Model) :
	dag_id = models.CharField('DAG_ID',max_length=100, default='')
	dag_name = models.CharField('DAG한글명',max_length=100, default='')
	service_name = models.CharField('서비스명',max_length=100, default='')
	remarks = models.CharField('비고',max_length=100, default='', null=True, blank=True)
	team = models.CharField('팀',max_length=100, default='')
	req_user = models.CharField('요청자',max_length=100, default='')

	class Meta :
		verbose_name = 'Airflow 관리'
		verbose_name_plural = 'Airflow 관리'
		db_table = 'cust_airflow_manage'

	def __str__(self) :
		return self.dag_name		

class Domain(models.Model) :
	domain_name = models.CharField('도메인명',max_length=100, default='')
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	exp_order = models.IntegerField('화면노출순서(0이면 노출 안됨)', blank=True, null=True, default=100)

	class Meta :
		verbose_name = '업무도메인관리 (고객/상품/주문....)'
		verbose_name_plural = '업무도메인관리 (고객/상품/주문....)'
		db_table = 'cust_domain'

	def __str__(self) :
		return self.domain_name

class Channel(models.Model) :
	channel_name = models.CharField('채널명',max_length=100, default=0)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	exp_order = models.IntegerField('화면노출순서(0이면 노출 안됨)', blank=True, null=True, default=100)

	class Meta :
		verbose_name = '채널구분 (기간계/정보계/MCPC)'
		verbose_name_plural = '채널구분 (기간계/정보계/MCPC)'
		db_table = 'cust_channel'

	def __str__(self) :
			return self.channel_name



class DataType(models.Model) :
	data_type = models.CharField('데이터유형',max_length=100)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_DataType_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_DataType_mod_user", db_column='id_mod_user', blank=True)
	exp_order = models.IntegerField('화면노출순서(0이면 노출 안됨)', blank=True, null=True, default=0)

	class Meta :
		verbose_name = '데이터유형구분 (real/staging...)'
		verbose_name_plural = '데이터유형구분 (real/staging...)'
		db_table = 'cust_data_type'

	def __str__(self) :
		return self.data_type

class Db(models.Model) :

	db_type = models.CharField('DBMS종류', max_length=100, null=True, blank=True)
	mod_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = '사용하는 DBMS'
		verbose_name_plural = '사용하는 DBMS'
		db_table = 'cust_db'

	def __str__(self) :
		return self.db_type

class DbType(models.Model) :
	id_db = models.ForeignKey(Db, verbose_name='DBMS위치', null=True, on_delete=models.PROTECT, db_column='id_db', blank=True)
	db_type = models.CharField('DBMS종류', max_length=100, null=True, blank=True)
	version = models.FloatField('버전', blank=True, null=True, help_text="숫자,소수점")
	# version = models.CharField('버전', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = '사용하는 DBMS 버전'
		verbose_name_plural = '사용하는 DBMS 버전'
		db_table = 'cust_db_type'

	def __str__(self) :
		return self.db_type + (( '(v.' + str(self.version) + ')' ) if self.version is not None else '')

class DbPosition(models.Model) :

	position = models.CharField('DBMS위치', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = 'DBMS 위치'
		verbose_name_plural = 'DBMS 위치'
		db_table = 'cust_db_position'

	def __str__(self) :
		return self.position

class HaCase(models.Model) :

	ha_case = models.CharField('HA유형', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = 'HA 유형'
		verbose_name_plural = 'HA 유형'
		db_table = 'cust_ha_case'

	def __str__(self) :
		return self.ha_case


class DbList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))




	db_use = models.CharField('DB용도', max_length=100)
	use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1', help_text="현재 운영되고 있는지... N 일 경우 모든 이벤트(변경관리, 모니터링 등)에서 제외됨")
	infra_op_yn = models.CharField('인프라팀운영여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1', help_text="인프라팀에서 운영하고 있는 시스템인지...")
	metareq_yn = models.CharField('DBA변경관리', null=True, blank=True, max_length=30, choices=choice_yn, default='0', help_text="Y 일 경우 테이블 변경 관리 신청 가능")
	gather_meta_yn = models.CharField('메타정보수집', null=True, blank=True, max_length=30, choices=choice_yn, default='0', help_text="Y 일 경우 테이블 메타 정보 수집 배치에 포함 됨")
	exp_order = models.IntegerField('화면노출순서', blank=True, null=True, default=999, help_text="화면에서 보이는 DB순서. ex) smtc : 1, webdb : 2")
	id_manager = models.ForeignKey(User, verbose_name='담당자', null=True, on_delete=models.PROTECT, db_column='id_manager', blank=True)
	id_channel = models.ForeignKey(Channel, verbose_name='채널명', null=True, on_delete=models.PROTECT, db_column='id_channel', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True,)
	db_desc = models.TextField('DB설명',max_length=4000, null=True, blank=True)
	privacy_yn = models.CharField('고객 개인정보', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	emp_privacy_yn = models.CharField('임직원 개인정보', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	id_dbtype = models.ForeignKey(DbType, verbose_name='DBMS종류', null=True, on_delete=models.PROTECT, db_column='id_dbtype', blank=True)
	id_dbposition = models.ForeignKey(DbPosition, verbose_name='DBMS위치', null=True, on_delete=models.PROTECT, db_column='id_dbposition', blank=True)
	db_ver = models.CharField('DBMS버전', max_length=100, null=True, blank=True)
	eos_yn = models.CharField('EOS여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	eos_dt = models.DateField('EOS일자', null=True, blank=True,)
	eos_explain = models.TextField('EOS조치방안',max_length=4000, null=True, blank=True)
	map_coords = models.CharField('Database MAP 좌표', max_length=100, null=True, blank=True, help_text="데이터베이스 지도에서의 마우스 클릭 좌표. null 입력 가능")
	disposal_dt = models.DateField('폐기일자', null=True, blank=True,)
	disposal_desc = models.TextField('폐기노트',max_length=4000, null=True, blank=True)

	class Meta :
		verbose_name = 'Database(서비스 레벨) 추가'
		verbose_name_plural = 'Database(서비스 레벨) 추가'
		ordering = ['db_use']
		db_table = 'cust_db_list'

	def __str__(self) :
		return self.db_use + " ("+self.id_dbtype.db_type+")"


class StdAttr(models.Model):

	choice_yn = ( (1,'대기중'),(0,'승인'),(2,'반려'))
	use_yn = ( ('1','사용'),('0','미사용') )

	id_stddomain = models.ForeignKey(StdDomain, verbose_name='표준도메인', on_delete=models.CASCADE, db_column='id_stddomain', blank=True, null=True)
	std_attr_kor = models.CharField('한글용어명',max_length=100, null=True, blank=True)
	std_attr_eng = models.CharField('영문용어명',max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.DO_NOTHING, db_column='id_reg_user', blank=True)
	accept_yn = models.IntegerField('승인여부', null=True, blank=True, choices=choice_yn, default='0')
	expl = models.TextField('설명', null=True, blank=True)
	reject_exp = models.CharField('반려사유', null=True, blank=True, max_length=100)
	use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=use_yn, default='1')
	csr_no = models.CharField('CSR번호', max_length=200, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)

	class Meta :
		verbose_name = '표준용어'
		verbose_name_plural = '표준용어'
		db_table = 'cust_std_attr'
	def __str__(self) :
		return self.std_attr_kor

class SendEmailTargetList(models.Model):

	choice_send_case = ( ('1','정기반영 - 일반'),
		          ('2','정기반영 - 개인정보 포함'),
		        )

	send_case = models.CharField('발송유형', null=True, blank=True, max_length=30, choices=choice_send_case, default='1')
	id_receive_user = models.ForeignKey(User, verbose_name='수인인', null=True, on_delete=models.CASCADE, db_column='id_receive_user', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)

	class Meta :
		verbose_name = 'DB정기반영 DEFAULT 이메일수신자'
		verbose_name_plural = 'DB정기반영 DEFAULT 이메일수신자'
		db_table = 'cust_email_target_list'
	def __str__(self) :
		return self.id_receive_user.first_name


class DBOwner(models.Model):

    id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.CASCADE, db_column='id_dblist', blank=True, null=True)
    owner = models.CharField('노출User명',max_length=100, default='')
    table_count = models.IntegerField('테이블개수', default=0)

    class Meta :
    	verbose_name = '메타관리 노출 OWNER'
    	verbose_name_plural = '메타관리 노출 OWNER'
    	db_table = 'cust_owner'
    	ordering = ('owner',)
    def __str__(self) :
    	return self.id_dblist.db_use + " : " + self.owner

class DBTablespace(models.Model):

    id_owner = models.ForeignKey(DBOwner, verbose_name='OWNER명', on_delete=models.CASCADE, db_column='id_owner', blank=True, null=True)
    id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.CASCADE, db_column='id_dblist', blank=True, null=True)
    tablespace_name = models.CharField('테이블스페이스명',max_length=100, default='')
    


    class Meta :
    	verbose_name = '테이블스페이스 매핑 : OWNER<->TABLESPACE'
    	verbose_name_plural = '테이블스페이스 매핑 : OWNER<->TABLESPACE'
    	db_table = 'cust_tablespace'
    def __str__(self) :
    	return self.tablespace_name




class DomainAndDbList(models.Model) :
	id_domain = models.ForeignKey(Domain, verbose_name='도메인명', on_delete=models.PROTECT, db_column='id_domain', blank=True, null=True)
	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', blank=True, null=True)
	it_manager = models.ManyToManyField(User, verbose_name='GSSHOP 담당자',  max_length=300,  blank=True, db_table = 'cust_domain_it_manager', related_name='domain_it_manager')
	dev_manager = models.ManyToManyField(User, verbose_name='개발 담당자',  max_length=300,  blank=True, db_table = 'cust_domain_dev_manager', related_name='domain_dev_manager')
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_DomainAndDbList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_DomainAndDbList_mod_user", db_column='id_mod_user', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True,)
	erd_user = models.CharField('ERD계정명',max_length=100, default='', null=True, blank=True,help_text="ex: ORD_ERD, PRD_ERD")

	class Meta :
		verbose_name = '업무도메인/담당자(테이블담당자) 매핑'
		verbose_name_plural = '업무도메인/담당자(테이블담당자) 매핑'
		db_table = 'cust_db_domain_mapping'

	def __str__(self) :
		return self.id_dblist.db_use + " :: " + self.id_domain.domain_name

class MonitorItem(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))
	monitor_level = (
				   ('0','SQL'),
		           ('1','OS'),
		         )


	# alphanumeric = RegexValidator(r'^[a-zA-Z_/ ]*$', '영문,언더바(_),스페이스만 입력 가능합니다.')
	
	# item_nm = models.CharField('모니터링 항목',max_length=100, validators=[alphanumeric], help_text=""""영문,언더바(_),스페이스만 입력 가능합니다.""", default="")
	item_nm = models.CharField('모니터링 항목',max_length=100, default="")
	monitor_level = models.CharField('모니터링Level', max_length=30, choices=monitor_level, default='0')	
	sms_message = models.CharField('알람 메시지',max_length=300, blank=True, null=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.CASCADE, db_column='id_reg_user', blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	exp_order = models.IntegerField('화면노출순서', blank=True, null=True, default=100)

	class Meta :
		verbose_name = '모니터링 Item 마스터'
		verbose_name_plural = '모니터링 Item 마스터'
		db_table = 'cust_monitor_item'		


	
	def __str__(self) :
		# return str(self.exp_order) + "." + self.id_dbtype.db_type + " : " + self.item_nm + " - " + self.lv2_item_nm
		return self.item_nm

class MonitorItemList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))
	risk_level = (
				   ('0','주의'),
		           ('1','심각'),
		           ('2','장애')
		         )

	compare_case = (
				   ('0','='),
		           ('1','<'),
		           ('2','>')
		         )


	relative_case = (
				   ('0','누적값'),
		           ('1','상대값'),
		         )

	alphanumeric = RegexValidator(r'^[a-zA-Z_]*$', '영문,언더바(_)만 입력 가능합니다.')

	id_monitoritem = models.ForeignKey(MonitorItem, verbose_name='모니터링ITEM명', null=True, on_delete=models.CASCADE, db_column='id_monitoritem', blank=True)
	id_dbtype = models.ForeignKey(DbType, verbose_name='DBMS종류', null=True, on_delete=models.CASCADE, db_column='id_dbtype', blank=True, help_text="SQL 모니터링 시 버전 Dependency 가 있는 경우만 상세 버전 선택, 나머지는 버전 미표기 선택")
	# item_nm = models.CharField('모니터링 항목',max_length=100)
	# lv2_item_nm = models.CharField('하위 모니터링 항목',max_length=100, validators=[alphanumeric], help_text=""""parameter 명 사용되며 알파벳+언더바만 사용 가능""", default="")
	# sms_message = models.CharField('알람 메시지',max_length=300, blank=True, null=True)
	use_yn = models.CharField('사용여부', max_length=30, choices=choice_yn, default='0')
	graph_yn = models.CharField('그래프표현여부', max_length=30, choices=choice_yn, default='0')
	compare_case = models.CharField('(임계치) 보다 모니터링값이 (부등호) ..하면 (리스크레벨)', max_length=30, choices=compare_case, null=True, blank=True)
	relative_case = models.CharField('누적값 여부', max_length=30, choices=relative_case, default=0)
	limit_value = models.CharField('Default임계치', max_length=100, null=True, blank=True)
	risk_level = models.CharField('Default 리스크레벨', max_length=30, choices=risk_level, null=True, blank=True)
	id_hacase = models.ForeignKey(HaCase, verbose_name='HA구분', null=True, on_delete=models.PROTECT, db_column='id_hacase', blank=True, help_text="MySQL Slave만 Seconday 선택, 나머지는 모두 Primary 선택")
	column_name = models.CharField('SQL내 모니터링 컬럼',max_length=30, blank=True, null=True, help_text=""""SELECT 되는 컬럼 Alias""")
	sql_text = models.TextField('모니터링 SQL', null=True, blank=True, help_text=""""SELECT 절에는 단일 항목, 하나의 ROW만 조회되도록 작성""")
	linux_cmd = models.TextField('Linux 명령어', null=True, blank=True, help_text=""""숫자만 리턴되도록 Script 입력""")
	unix_cmd = models.TextField('Unix 명령어', null=True, blank=True, help_text=""""숫자만 리턴되도록 Script 입력""")
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.CASCADE, db_column='id_reg_user', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	

	class Meta :
		verbose_name = '모니터링 Item 상세'
		verbose_name_plural = '모니터링 Item 상세'
		db_table = 'cust_monitor_item_list'
		ordering = ['id_dbtype',]


	def __str__(self) :
		# return str(self.exp_order) + "." + self.id_dbtype.db_type + " : " + self.item_nm + " - " + self.lv2_item_nm
		return self.id_monitoritem.get_monitor_level_display() + " : " + self.id_monitoritem.item_nm





class DbDetail(models.Model) :
	choice_yn = ( ('1','Y'),('0','N'))

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', null=True, on_delete=models.CASCADE, db_column='id_dblist', to_field='id')
	use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1', help_text="서버 사용 여부. N 일 경우 모든 이벤트(모니터링, Alert 등)에서 제외")	
	alert_yn = models.CharField('Alert여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1', help_text="Alert 여부. N 일 경우 Alert 만 비활성화")
	db_order = models.IntegerField('DB노드번호', default=1, help_text="ex) SMTC11 : 1, SMTC12 : 2, Master : 1, Slave : 2")
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd')
	db_nm = models.CharField('DB명', max_length=100, help_text="MySQL 일 경우 show database 명 입력")
	inst_nm = models.CharField('인스턴스명', max_length=100, help_text="MySQL 일 경우 show database 명 입력")
	host_nm = models.CharField('호스트명', max_length=100, blank=True)
	id_hacase = models.ForeignKey(HaCase, verbose_name='HA구분', null=True, on_delete=models.PROTECT, db_column='id_hacase')
	id_monitoritemlist = models.ManyToManyField(MonitorItemList, verbose_name='모니터링 리스트', blank=True,  through='DBDetailMonitorItemList')
	svr_ip = models.CharField('서버ip', max_length=100, null=True, blank=True)
	svc_ip = models.CharField('서비스ip', max_length=100, null=True, blank=True)
	port = models.CharField('포트', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	tns_desc = models.TextField('DB접속정보(TNS,EndPoint등)', max_length=4000, null=True, blank=True)
	id_sms_receive_user = models.ManyToManyField(User, verbose_name='모니터링 SMS 수신 인원(복수 선택 가능)',  max_length=300,  blank=True, db_table='cust_monitor_sms_receive_user', related_name='cust_monitor_sms_receive_user', help_text="""DBA 외에 모니터링 알람을 받는 담당자""")
	id_dbposition = models.ForeignKey(DbPosition, verbose_name='DBMS위치', null=True, on_delete=models.SET_NULL, db_column='id_dbposition', blank=True)

	sync_db_pos  = models.CharField('(sync) DBMS위치', max_length=100, blank=True, null=True)
	sync_oper_cd  = models.CharField('(sync) 운영 구분', max_length=100, blank=True, null=True)
	sync_hacase  = models.CharField('(sync) HA구분', max_length=100, blank=True, null=True)
	sync_db_order  = models.CharField('(sync) DB별순서', max_length=100, blank=True, null=True)	
	sync_hostnm  = models.CharField('(sync) 호스트명', max_length=100, blank=True, null=True)
	sync_srv_ip  = models.CharField('(sync) 서버IP', max_length=100, blank=True, null=True)
	sync_svc_ip  = models.CharField('(sync) 서비스IP', max_length=100, blank=True, null=True)
	sync_db_port  = models.CharField('(sync) 포트', max_length=100, blank=True, null=True)
	sync_db_nm  = models.CharField('(sync) DB명', max_length=100, blank=True, null=True)
	sync_db_type  = models.CharField('(sync) DB타입', max_length=100, blank=True, null=True)
	sync_db_edition  = models.CharField('(sync) 에디션', max_length=100, blank=True, null=True)
	sync_db_version  = models.CharField('(sync) 버전', max_length=100, blank=True, null=True)
	sync_db_eos  = models.CharField('(sync) DB EOS', max_length=100, blank=True, null=True)
	sync_os_version  = models.CharField('(sync) OS버전', max_length=100, blank=True, null=True)
	sync_os_patch  = models.CharField('(sync) OS패치', max_length=100, blank=True, null=True)
	sync_os_cpu_type  = models.CharField('(sync) CPU타입', max_length=100, blank=True, null=True)
	sync_os_cpu_performance  = models.CharField('(sync) CPU 성능', max_length=100, blank=True, null=True)
	sync_os_server_active  = models.CharField('(sync) 서버 활성화', max_length=100, blank=True, null=True)
	sync_os_cpu_socket = models.CharField('(sync) CPU 소켓수', max_length=100, blank=True, null=True)
	sync_os_cpu_socket_core  = models.CharField('(sync) 소켓당 코어수', max_length=100, blank=True, null=True)
	sync_os_cpu_total_core  = models.CharField('(sync) 전체 코어수', max_length=100, blank=True, null=True)
	sync_os_real_use_core  = models.CharField('(sync) 실사용 코어수', max_length=100, blank=True, null=True)
	sync_os_thread_factor  = models.CharField('(sync) 쓰레드 팩터', max_length=100, blank=True, null=True)
	sync_os_real_use_thread  = models.CharField('(sync) 실사용 쓰레드수', max_length=100, blank=True, null=True)
	sync_license_std  = models.CharField('(sync) 라이선스정책 (Oracle)', max_length=100, blank=True, null=True)
	sync_license_use  = models.CharField('(sync) 라이선스 정책적용', max_length=100, blank=True, null=True)
	sync_os_memory  = models.CharField('(sync) 메모리', max_length=100, blank=True, null=True)
	sync_license_charge_yn  = models.CharField('(sync) 라이선스 과금유무', max_length=100, blank=True, null=True)
	sync_server_manage  = models.CharField('(sync) 서버 관리', max_length=100, blank=True, null=True)


	class Meta :
		verbose_name = 'Database(서버 레벨) 추가'
		verbose_name_plural = 'Database(서버 레벨) 추가'
		db_table = 'cust_db_detail'


	def __str__(self) :
		# return self.oper_cd.oper_cd + " " + self.id_dblist.db_use + "(" + self.host_nm + ", "+ self.id_hacase.ha_case + ")"
		return self.oper_cd.oper_cd + " " + self.id_dblist.db_use + " 노드" + str(self.db_order) + " (" + self.id_dblist.id_dbtype.db_type + ", " + self.id_hacase.ha_case + ")"

class OsUser(models.Model) :
	choice_yn = ( ('1','Y'),('0','N'))

	id_dbdetail = models.ForeignKey(DbDetail, verbose_name='DB상세', on_delete=models.CASCADE, db_column='id_dbdetail')
	user_name  = models.CharField('OS계정명', max_length=100, blank=True, null=True)
	password  = SafeCharField('패스워드', max_length=128, cipher_class=AesCipher, password=settings.SECRET_KEY, default='')
	use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1')	
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.CASCADE, db_column='id_mod_user', blank=True)

	class Meta :
		verbose_name = 'OS계정정보'
		verbose_name_plural = 'OS계정정보'
		db_table = 'cust_os_user'

	def __str__(self) :		

		return self.user_name + " (" + str(self.id_dbdetail) + ")"

class DbUser(models.Model) :
	choice_yn = ( ('1','Y'),('0','N'))

	id_dblist = models.ForeignKey(DbList, verbose_name='DB', on_delete=models.PROTECT, db_column='id_dblist')
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd')
	username  = models.CharField('DB계정명', max_length=100, null=True)
	password  = SafeCharField('패스워드', max_length=128, cipher_class=AesCipher, password=settings.SECRET_KEY, default='', help_text="""* 개발 : dev#DB계정명(알파벳만)!@34<br>* 운영 : gs#DB계정명(알파벤만)!@34""")
	conn_ip  = models.CharField('Source IP', max_length=100, null=True, blank=False, default="%", help_text="""ORACLE : % 입력, Mysql Mariadb일 경우 접근하는 Source IP 입력""")
	req_reason  = models.TextField('생성목적', max_length=1000, null=True)
	use_yn = models.CharField('사용여부', null=True, max_length=30, choices=choice_yn, default='1')	
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	id_req_user = models.ForeignKey(User, verbose_name='요청자', null=True, on_delete=models.PROTECT, db_column='id_req_user', related_name="DbUser_id_req_user")
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', related_name="DbUser_id_reg_user",blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, db_column='id_mod_user', related_name="DbUser_id_mod_user",blank=True)
	drop_yn = models.CharField('삭제여부', null=True, max_length=30, choices=choice_yn, default='0')	
	drop_dtm = models.DateTimeField('삭제일자', null=True, blank=True)

	class Meta :
		verbose_name = 'DB (서비스)계정정보'
		verbose_name_plural = 'DB (서비스)계정정보'
		db_table = 'cust_db_user'

	def __str__(self) :		

		return self.username + " (" + str(self.id_dblist.db_use) + ")"		




class DBDetailMonitorItemList(models.Model) :
	choice_yn = ( ('1','Y'),('0','N'))

	risk_level = (
				   ('0','주의'),
		           ('1','심각'),
		           ('2','장애')
		         )

	compare_case = (
				   ('0','='),
		           ('1','<'),
		           ('2','>')
		         )

	id_dbdetail = models.ForeignKey(DbDetail, verbose_name='DB상세', on_delete=models.CASCADE, db_column='id_dbdetail')
	id_monitoritemlist = models.ForeignKey(MonitorItemList, verbose_name='모니터아이템리스트', on_delete=models.CASCADE, db_column='id_monitoritemlist')
	compare_case = models.CharField('(임계치) 보다 모니터링값이 (부등호) ..하면 (리스크레벨)', max_length=30, choices=compare_case, default='0', null=True, blank=True)
	limit_value = models.CharField('임계치', max_length=100, null=True, blank=True, default='0',help_text="""Health Cheack 일 경우 OPEN 으로 입력""")
	risk_level = models.CharField('리스크레벨', max_length=30, choices=risk_level, default='0', null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.CASCADE, db_column='id_reg_user', blank=True, related_name="DBDetailMonitorItemList_reg_user", )
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.CASCADE, db_column='id_mod_user', blank=True, related_name="DBDetailMonitorItemList_mod_user", )
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	note1 = models.CharField('노트1', max_length=300, null=True, blank=True)

	class Meta :
		# verbose_name = '모니터링 항목 등록 - 한 개 이상 등록 시 모니터링 활성화 ( Health Check 일 경우 임계치는 OPEN 입력 )'
		# verbose_name_plural = '모니터링 항목 등록 - 한 개 이상 등록 시 모니터링 활성화 ( Health Check 일 경우 임계치는 OPEN 입력 )'
		verbose_name = 'DB서버 별 모니터링 상세'
		verbose_name_plural = 'DB서버 별 모니터링 상세'
		db_table = 'cust_dbdetail_monitoritemlist'

		



	def __str__(self) :
		return self.id_dbdetail.id_dblist.db_use + " : " + self.id_monitoritemlist.id_monitoritem.item_nm

class MonitorItemLog(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	id_dbdetailmonitoritemlist = models.ForeignKey(DBDetailMonitorItemList, verbose_name='모니터링타겟', on_delete=models.CASCADE, db_column='id_dbdetailmonitoritemlist', blank=True,null=True)
	monitor_value = models.CharField('값(value)',max_length=300, blank=True,null=True)
	error_yn = models.CharField('에러여부', max_length=30, choices=choice_yn, default='0')
	error_msg = models.TextField('에러메시지', null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	curr_yn = models.CharField('현재여부', max_length=30, choices=choice_yn, default='0')
	elapsed_time = models.FloatField('수행시간(초)', blank=True, null=True, default=0)

	class Meta :
		verbose_name = '모니터링 LOG'
		verbose_name_plural = '모니터링 LOG'
		db_table = 'cust_monitor_item_log'		

class MonitorManagement(models.Model) :

	choice_yn = ( ('1','ON'),('0','OFF'))

	monitor_name = models.CharField('모니터링명', max_length=100, null=True, blank=True)	
	id_dbdetail = models.ManyToManyField(DbDetail, verbose_name='모니터링DB선택', 
		                                           blank=True, 
		                                           db_table='cust_monitorm_dbdetail', 
		                                           related_name='cust_monitorm_dbdetail', 
		                                           help_text="모니터링이 필요한 DB를 선택하세요",
		                                           limit_choices_to=Q(id_hacase__in=[1,2]) & Q(oper_cd__in=[3,4]))	
	monitor_yn = models.CharField('전체 모니터링 켜기/끄기', max_length=30, choices=choice_yn, default='0')
	alert_yn = models.CharField('전체 Slack(Alert) 켜기/끄기 - DB작업 시 OFF', max_length=30, choices=choice_yn, default='0')
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True)	
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.CASCADE, db_column='id_mod_user', blank=True)

	class Meta :
		verbose_name = '모니터링관리'
		verbose_name_plural = '모니터링관리'
		db_table = 'cust_monitor_management'

	def __str__(self) :
		return self.monitor_name

class MonitorTablespace(models.Model) :
	id_dbdetail = models.ForeignKey(DbDetail, verbose_name='DB상세', on_delete=models.CASCADE, db_column='id_dbdetail', blank=True, null=True)
	tablespace_name = models.CharField('테이블스페이스명',max_length=100, default='')
	limit_value = models.IntegerField('임계치(%)', null=True, blank=True, default='95')
	explain = models.CharField('비고', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.CASCADE, db_column='id_mod_user', blank=True)

	class Meta :
		verbose_name = '테이블스페이스 모니터링, 임계치 조정'
		verbose_name_plural = '테이블스페이스 모니터링, 임계치 조정'
		db_table = 'cust_monitor_tablespace'

	def __str__(self) :
		return self.id_dbdetail.id_dblist.db_use + " : " + self.tablespace_name

class MonitorTablespaceLog(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	id_dbdetail = models.ForeignKey(DbDetail, verbose_name='DB상세', on_delete=models.CASCADE, db_column='id_dbdetail', blank=True, null=True)
	tablespace_name = models.CharField('테이블스페이스명',max_length=100, default='')
	total = models.CharField('전체사이즈',max_length=100, null=True, blank=True)
	free = models.CharField('FREE사이즈',max_length=100, null=True, blank=True)
	used = models.CharField('사용사이즈',max_length=100, null=True, blank=True)
	usage_percent = models.CharField('사용율',max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	curr_yn = models.CharField('현재여부', max_length=30, choices=choice_yn, default='0')

	class Meta :
		verbose_name = '모니터링테이블스페이스로그'
		verbose_name_plural = '모니터링테이블스페이스로그'
		db_table = 'cust_monitor_tablespace_log'

	def __str__(self) :
		return self.id_dbdetail.id_dblist.db_use + " : " + self.tablespace_name



class ObjectList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', to_field='id', blank=True)
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd', blank=True)
	db_use = models.CharField('db용도', max_length=100, blank=True, null=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', blank=True, null=True)
	owner = models.CharField('소유자', max_length=100)
	object_name = models.CharField('오브젝트', max_length=100, blank=True)
	subobject_name = models.CharField('서브오브젝트', max_length=100, null=True, blank=True)
	object_type = models.CharField('오브젝트타입', max_length=100, blank=True)
	status = models.CharField('상태', max_length=100, blank=True)
	created = models.DateTimeField('생성일자', blank=True, null=True)
	last_ddl_time = models.DateTimeField('변경일자', blank=True, null=True)
	drop_yn = models.CharField('삭제여부', max_length=30, choices=choice_yn, default='0', blank=True)
	drop_dtm = models.DateTimeField('삭제일자', blank=True, null=True)

	class Meta :
		verbose_name = 'Object 리스트'
		verbose_name_plural = 'Object 리스트'
		db_table = 'cust_object_list'

	def __str__(self) :
		return "{db_nm} / {owner} / {object_name}".format(db_nm=self.db_use,
														 owner=self.owner,
														 object_name=self.object_name,)

class TableList(models.Model) :



	
	choice_yn = ( ('1','Y'),('0','N'))
	# data_type = (
	# 				('0','실시간 데이터'),
	# 				('1','스테이징 데이터'),
	# 				('2','1차 가공 데이터'),
	# 		)

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', to_field='id', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_TableList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_TableList_mod_user", db_column='id_mod_user', blank=True)
	owner = models.CharField('소유자', max_length=100)
	table_name = models.CharField('테이블 물리명', max_length=100, blank=True)
	comments = models.CharField('테이블 논리명', max_length=4000, blank=True, null=True)
	tablespace_name = models.CharField('테이블스페이스명', max_length=100, blank=True, null=True)
	num_rows = models.IntegerField('Row개수', blank=True, null=True, default=0)
	last_analyzed = models.DateTimeField('Last_Analyzed', blank=True, null=True)
	created = models.DateTimeField('Created', blank=True, null=True)
	last_ddl_time = models.DateTimeField('Last_DDL_Time', blank=True, null=True)
	total_mb = models.BigIntegerField('사이즈(MB)', blank=True, null=True, default=0)
	lob_mb = models.BigIntegerField('LOB사이즈(MB)', blank=True, null=True, default=0)
	id_user_it_manager = models.ForeignKey(User, verbose_name='IT담당자', null=True, on_delete=models.PROTECT, related_name="it_manager", db_column='id_user_it_manager', blank=True)
	id_user_dev_manager = models.ForeignKey(User, verbose_name='개발담당자', null=True, on_delete=models.PROTECT, related_name="dev_manager", db_column='id_user_dev_manager', blank=True)
	# id_domainlist = models.ForeignKey(DomainList, verbose_name='업무도메인명', on_delete=models.PROTECT, db_column='id_domainlist', blank=True,null=True)
	id_domain = models.ForeignKey(Domain, verbose_name='업무도메인명', on_delete=models.PROTECT, db_column='id_domain', blank=True,null=True)
	drop_yn = models.CharField('삭제여부', max_length=30, choices=choice_yn, default='0', blank=True)
	drop_dtm = models.DateTimeField('삭제일자', blank=True, null=True)
	cdc_yn = models.CharField('CDC대상여부', max_length=30, choices=choice_yn, default='0',blank=True, null=True)
	table_explain = models.TextField('설명',max_length=4000, null=True, blank=True)
	sql_exp_column = models.CharField('SQL노출컬럼', max_length=200, null=True, blank=True)
	# data_search_psbl_yn = models.CharField('데이터검색가능여부', max_length=100, null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	pk_column = models.CharField('PK 컬럼', max_length=100, blank=True, null=True)
	id_tablelist_parent_table = models.ForeignKey("self", verbose_name='부모테이블',  max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist_parent_table')
	id_tablelist_member_table = models.ManyToManyField("self", verbose_name='구성 테이블',  max_length=100,  blank=True, db_column='id_tablelist_member_table', db_table = 'cust_member_table')
	config_sql = models.TextField('집계SQL',null=True, blank=True)
	exp_order = models.IntegerField('화면노출순서(0이면 노출 안됨)', blank=True, null=True, default=1000)
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd', blank=True)
	db_use = models.CharField('db용도', max_length=100, blank=True, null=True)
	id_datatype = models.ForeignKey(DataType, verbose_name='DATA유형', on_delete=models.PROTECT, db_column='id_datatype',null=True, blank=True)
	secu_yn = models.CharField('테이블 레벨 개인정보여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0',help_text="""컬럼 중 하나라도 개인정보 컬럼이면 "Y" 체크해주세요.""")




	class Meta :
		verbose_name = 'Table 관리'
		verbose_name_plural = 'Table 관리'
		db_table = 'cust_table_list'

	def __str__(self) :
		return "{table_name}".format(table_name=self.table_name,)

class UserList(models.Model) :


	account_status = (
					('0','OPEN'),
					('1','LOCK'),
		)

	request_status = (
					('0','미신청'),
					('1','신청중'),
		)

	choice_yn = ( ('1','Y'),('0','N'))

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.CASCADE, db_column='id_dblist', to_field='id', blank=True)
	db_use = models.CharField('db용도', max_length=100, blank=True, null=True)
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd', blank=True)
	username = models.CharField('계정명', max_length=100, null=True, blank=True)
	id_user_name = models.ForeignKey(User, verbose_name='이름', null=True, on_delete=models.CASCADE, db_column='id_user_name', blank=True)
	status = models.CharField('계정상태', max_length=100, choices=account_status, default='0', null=True, blank=True)
	created = models.DateTimeField('생성일자', auto_now_add=True)
	profile = models.CharField('프로파일명', max_length=100, null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	request_status = models.CharField('신청상태', max_length=100, choices=request_status, default='0', null=True, blank=True)
	drop_yn = models.CharField('삭제여부', max_length=30, choices=choice_yn, default='0', blank=True)
	drop_dtm = models.DateTimeField('삭제일자', null=True, blank=True)
	conn_ip  = models.CharField('접속IP', max_length=100, null=True, blank=True)

	class Meta :
		verbose_name = 'User 리스트'
		verbose_name_plural = 'User 리스트'
		db_table = 'cust_user_list'

	def __str__(self) :
		return "{name}({username})".format(name=self.id_user_name.first_name,username=self.username)

class UserRequestAccountOpenHist(models.Model) :



	id_userlist = models.ForeignKey(UserList, verbose_name='User명', on_delete=models.CASCADE, db_column='id_userlist')
	id_approver = models.ForeignKey(User, verbose_name='승인자', null=True, on_delete=models.CASCADE, db_column='id_approver', blank=True)
	approv_dtm = models.DateTimeField('승인일자',blank=True,null=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.CASCADE, related_name="id_reg_user", blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)

	class Meta :
		verbose_name = '계정활성화신청이력'
		verbose_name_plural = '계정활성화신청이력'
		db_table = 'cust_user_request_account_open_hist'



class UserRequestTabPrivHist(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	id_userlist = models.ForeignKey(UserList, verbose_name='User명', on_delete=models.CASCADE, db_column='id_userlist', null=True, blank=True)
	id_objectlist = models.ForeignKey(ObjectList, verbose_name='오브젝트명', on_delete=models.CASCADE, db_column='id_obejctlist', null=True, blank=True)
	id_approver = models.ForeignKey(User, verbose_name='승인자', null=True, on_delete=models.CASCADE, related_name="id_approver_priv", db_column='id_approver', blank=True)
	approv_dtm = models.DateTimeField('승인일자',blank=True,null=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.CASCADE, related_name="id_reg_user_priv", blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	priv = models.CharField('권한', max_length=100, null=True, blank=True)
	object_type = models.CharField('오브젝트타입', max_length=100, null=True, blank=True)
	req_reason = models.TextField('신청사유',max_length=4000, null=True, blank=True)
	approv_yn = models.CharField('승인여부', max_length=30, choices=choice_yn, default='0')

	use_yn = models.CharField('사용여부', max_length=30, choices=choice_yn, default='1')


	class Meta :
		verbose_name = '테이블권한신청'
		verbose_name_plural = '테이블권한신청'
		db_table = 'cust_user_request_tab_priv_hist'



class MetaReq(models.Model) :

	check_prod_exec_yn = ( ('1','정기반영 대상'),('0','대상 아님'))

	choice_yn = ( ('1','Y'),('0','N'))

	ok_yn = ( ('0','승인 전'), ('1','승인(반영)'),('2','반려'))

	choice_obj_class =   (
							('', '오브젝트 유형 선택'),
							# ('1', 'TABLE(표준)'),
							('2', 'TABLE'),
							('3', 'INDEX'),
							('4', '권한'),
							('5', 'PROCEDURE'),
							('6', 'FUNCTION'),
							('7', 'SEQUENCE'),
							('8', 'PACKAGE'),
							('9', '기타'),
						  )

	choice_obj_new =   (
							('', '신청 유형 선택'),
							('1', '변경'),
							('2', '신규'),
							('3', '삭제'),
						  )

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', null=True)
	id_tablelist = models.ForeignKey(TableList, verbose_name='테이블명', max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist')
	title = models.CharField('제목', max_length=200, null=True, blank=True)
	csr = models.CharField('CSR', max_length=200, null=True, blank=True)
	table_name = models.CharField('테이블 물리명', max_length=100, null=True, blank=True)
	table_comments = models.CharField('테이블 논리명', max_length=100, null=True, blank=True)
	obj_class = models.CharField('오브젝트 유형',  null=True, max_length=30, choices=choice_obj_class)
	obj_new = models.CharField('변경 유형',  null=True, max_length=30, choices=choice_obj_new)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	mod_dtm = models.DateTimeField('수정일자', null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='요청자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)
	req_contents = models.TextField('요청자 내용', null=True)
	req_script = models.TextField('개발자 요청 스크립트', null=True, blank=True)
	script = models.TextField('DBA Script', null=True, blank=True)
	script_dtm = models.DateTimeField('Script저장일시', null=True, blank=True)
	id_script_reg_user = models.ForeignKey(User, verbose_name='Script등록자', null=True, on_delete=models.PROTECT, db_column='id_script_reg_user', blank=True, related_name="metareq_id_script_reg_user")
	storage_cycle = models.IntegerField('보관주기', null=True, blank=True)
	storage_cycle_column = models.CharField('기준컬럼', max_length=100, null=True, blank=True)
	id_domainanddblist = models.ForeignKey(DomainAndDbList, verbose_name='도메인명', on_delete=models.SET_NULL, db_column='id_domainanddblist', blank=True, null=True)
	id_pl_dev = models.ForeignKey(User, verbose_name='PL개발승인자', db_column='id_pl_dev', related_name="metareq_id_pl_dev", null=True, on_delete=models.PROTECT,  blank=True)
	id_pl_prod = models.ForeignKey(User, verbose_name='PL운영승인자', db_column='id_pl_prod', related_name="metareq_id_pl_prod", null=True, on_delete=models.PROTECT,  blank=True)
	id_dba_dev = models.ForeignKey(User, verbose_name='DBA개발승인자', db_column='id_dba_dev', related_name="metareq_id_dba_dev", null=True, on_delete=models.PROTECT,  blank=True)
	id_dba_prod = models.ForeignKey(User, verbose_name='DBA운영승인자', db_column='id_dba_prod', related_name="metareq_id_dba_prod", null=True, on_delete=models.PROTECT,  blank=True)
	id_da_dev = models.ForeignKey(User, verbose_name='DA개발승인자', db_column='id_da_dev', related_name="metareq_id_da_dev", null=True, on_delete=models.PROTECT,  blank=True)
	id_req_prod = models.ForeignKey(User, verbose_name='운영반영요청자', db_column='id_req_prod', related_name="metareq_id_req_prod", null=True, on_delete=models.PROTECT,  blank=True)
	pl_dev_yn = models.CharField('PL개발승인여부', max_length=200, choices=ok_yn, default='0')
	dba_dev_yn = models.CharField('DBA개발승인여부', max_length=200, choices=ok_yn, default='0')
	da_dev_yn = models.CharField('DA개발승인승인여부', max_length=200, choices=ok_yn, default='0')
	req_prod_yn = models.CharField('운영반영요청여부', max_length=200, choices=ok_yn, default='0')
	pl_prod_yn = models.CharField('PL운영승인여부', max_length=200, choices=ok_yn, default='0')
	dba_prod_yn = models.CharField('DBA 운영 반영 여부', max_length=200, choices=ok_yn, default='0')
	pl_dev_comment = models.CharField('PL개발승인의견', max_length=1000, null=True)
	pl_prod_comment = models.CharField('PL운영승인의견', max_length=1000, null=True)
	dba_dev_comment = models.CharField('DBA개발승인의견', max_length=1000, null=True)
	dba_prod_comment = models.CharField('DBA운영승인의견', max_length=1000, null=True)
	da_dev_comment = models.CharField('DA개발승인의견', max_length=1000, null=True)
	req_prod_comment = models.CharField('운영반영요청의견', max_length=1000, null=True)
	pl_dev_dtm = models.DateTimeField('PL개발승인시간', null=True, blank=True)
	pl_prod_dtm = models.DateTimeField('PL운영승인시간', null=True, blank=True)
	dba_dev_dtm = models.DateTimeField('DBA개발승인시간', null=True, blank=True)
	dba_prod_dtm = models.DateTimeField('DBA운영승인시간', null=True, blank=True)
	da_dev_dtm = models.DateTimeField('DA개발승인시간', null=True, blank=True)
	req_prod_dtm = models.DateTimeField('운영반영요청시간', null=True, blank=True)
	dist_dtm = models.DateTimeField('배포희망일자', null=True, blank=True)
	check_prod_exec_yn = models.CharField('금주 정기 반영 대상 여부', max_length=200, choices=check_prod_exec_yn, default='0')





	class Meta :
		verbose_name = '메타관리(테이블변경신청)'
		verbose_name_plural = '메타관리(테이블변경신청)'
		db_table = 'cust_meta_req'

	def __str__(self) :
		return self.title

# class MonitorManage(DbDetail):
#     class Meta:
#         proxy = True
#         verbose_name = '모니터링관리'
#         verbose_name_plural = '모니터링관리'

class MetaReqWeekDay(MetaReq):
    class Meta:
        proxy = True
        verbose_name = '정기반영 대상 지정'
        verbose_name_plural = '정기반영 대상 지정'

class MetaReqList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))
	privacy_list = ( ('0',''),('1','개인정보'))

	div = models.CharField('구분',  null=True, blank=True, max_length=30)
	id_metareq = models.ForeignKey(MetaReq, verbose_name='메타요청', max_length=100, null=True, blank=True, on_delete=models.CASCADE, db_column='id_metareq')
	id_tablelist = models.ForeignKey(TableList, verbose_name='테이블명', max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist')
	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', blank=True, null=True)
	column_id = models.IntegerField('컬럼순서', null=True, blank=True)
	col_comments = models.CharField('컬럼코멘트', max_length=4000, null=True, blank=True)
	pk_yn = models.CharField('PK여부',  null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	not_null = models.CharField('NOT NULL',  null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	column_name = models.CharField('컬럼명', max_length=100, null=True, blank=False)
	data_type = models.CharField('데이터타입', max_length=100, null=True, blank=True)
	change_list = models.CharField('변경사항', max_length=100, null=True, blank=False)
	change_reason = models.TextField('비고', null=True, blank=True)
	privacy_list = models.CharField('개인정보',  null=True, blank=True, max_length=30, choices=privacy_list, default='0')
	data_default = models.CharField('default값', max_length=100, null=True, blank=True)


	class Meta :
		verbose_name = '메타변경요청상세'
		verbose_name_plural = '메타변경요청상세'
		db_table = 'cust_meta_req_list'

	# def __str__(self) :
	# 	return self.id_tablelist.table_name



class ColumnList(models.Model) :


	choice_yn = ( ('1','Y'),('0','N'))
	column_type = ( ('2','개별코드'),('1','공통코드'),('0','일반컬럼'))

	id_tablelist = models.ForeignKey(TableList, verbose_name='테이블명', max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist')
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	column_name = models.CharField('컬럼명', max_length=100, null=True, blank=False)
	col_comments = models.CharField('컬럼코멘트', max_length=4000, null=True, blank=True)
	column_id = models.IntegerField('컬럼순서', null=True, blank=True)
	pk_yn = models.CharField('PK여부',  null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	data_type = models.CharField('데이터타입', max_length=100, null=True, blank=True)
	personal_info = models.CharField('개인정보유무', max_length=100, null=True, blank=True, choices=choice_yn)
	secu_yn = models.CharField('컬럼 레벨 개인정보여부', null=True, blank=True, max_length=30, choices=choice_yn)
	secu_typ = models.CharField('개인정보타입', max_length=100, null=True, blank=True)
	secu_tds_yn = models.CharField('데이터변조여부', null=True, blank=True, max_length=30, choices=choice_yn)
	secu_tds_enc_typ = models.CharField('데이터변조타입', max_length=100, null=True, blank=True)
	secu_pis_yn = models.CharField('유효기간제여부',  null=True, blank=True, max_length=30, choices=choice_yn)
	secu_pin_yn = models.CharField('고유식별번호여부',  null=True, blank=True, max_length=30, choices=choice_yn)
	secu_remark = models.TextField('비고', max_length=4000, null=True, blank=True)
	column_explain = models.TextField('설명',max_length=4000, null=True, blank=True)
	biz_label = models.CharField('업무용어', max_length=100, null=True, blank=True)
	biz_path = models.CharField('업무경로', max_length=100, null=True, blank=True)
	id_tablelist_code_table = models.ForeignKey(TableList, verbose_name='코드테이블', related_name="id_tablelist_code_table", max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist_code_table')
	code_key = models.CharField('매핑코드값', max_length=100, null=True, blank=True)
	sql_text = models.TextField('관련SQL',max_length=4000, null=True, blank=True)
	column_type = models.CharField('컬럼타입', max_length=100, null=True, blank=True, choices=column_type, default='0')
	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', to_field='id',null=True, blank=True)
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd', blank=True)
	owner = models.CharField('소유자', max_length=100,null=True, blank=True)
	table_name = models.CharField('테이블 물리명', max_length=100,null=True, blank=True)
	comments = models.CharField('테이블 논리명', max_length=4000, blank=True, null=True)
	db_use = models.CharField('db용도', max_length=100, blank=True, null=True)
	drop_yn = models.CharField('삭제여부', max_length=30, choices=choice_yn, default='0', blank=True)
	drop_dtm = models.DateTimeField('삭제일자', blank=True, null=True)
	data_default = models.CharField('default값', max_length=100,null=True, blank=True)
	not_null = models.CharField('NotNull여부', max_length=30, choices=choice_yn, default='0', blank=True)

	# id_columnlist = models.ManyToManyField("self", verbose_name='관련 검색어',  max_length=100,  blank=True, db_column='id_columnlist')


	# def table_nm(self) :
	# 	return self.id_tablelist.table_name
	# table_name.short_description = 'TABLE 물리명'

	# def comments(self) :
	# 	return self.id_tablelist.comments
	# table_name.short_description = 'TABLE 논리명'

	# def db_use(self) :
	# 	return self.id_tablelist.id_dblist.db_use
	# db_use.short_description = 'DB명'


	class Meta :
		verbose_name = 'Column 리스트'
		verbose_name_plural = 'Column 리스트'
		db_table = 'cust_column_list'

	def __str__(self) :
		return self.column_name

class GrantList(models.Model) :

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', null=True)
	oper_cd = models.ForeignKey(OperCd, verbose_name='운영구분', null=True, on_delete=models.PROTECT, db_column='oper_cd', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
	id_userlist = models.ForeignKey(UserList, verbose_name='User명', on_delete=models.CASCADE, db_column='id_userlist', null=True, blank=True)
	grantee = models.CharField('grantee', max_length=100, null=True, blank=True)
	id_tablelist = models.ForeignKey(TableList, verbose_name='테이블명', max_length=100, null=True, blank=True, on_delete=models.PROTECT, db_column='id_tablelist')
	owner = models.CharField('owner', max_length=100, null=True, blank=True)
	table_name = models.CharField('table_name', max_length=100, null=True)
	privilege = models.CharField('privilege', max_length=100, null=True, blank=True)
	granted_role = models.CharField('granted_role', max_length=100, null=True, blank=True)

	class Meta :
		verbose_name = '권한 리스트'
		verbose_name_plural = '권한 리스트'
		db_table = 'cust_grant_list'


class DataList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))
	privacy_choice_yn = ( ('1','존재'),('0','없음'))
	confirm_yn = ( ('1','승인'),('0','승인대기'),('2','반려'))
	realoretl_yn = ( ('1','실시간'),('0','분석'))

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.PROTECT, db_column='id_dblist', null=True, default=39, help_text=""""데이터허브DB"를 제외한 나머지 DB는 성능 승인을 받은 후 수행할 수 있습니다.""")
	id_domain = models.ForeignKey(Domain, verbose_name='업무도메인명', on_delete=models.PROTECT, db_column='id_domain', null=True, default=17)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_DataList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_DataList_mod_user", db_column='id_mod_user', blank=True)
	id_prov_user1 = models.ForeignKey(User, verbose_name='2차 승인(보안)', null=True, on_delete=models.PROTECT, related_name="User_DataList_prov_user1", db_column='id_prov_user1', blank=True)
	id_prov_user2 = models.ForeignKey(User, verbose_name='1차 승인(성능)', null=True, on_delete=models.PROTECT, related_name="User_DataList_prov_user2", db_column='id_prov_user2', blank=True)
	prov_yn1 = models.CharField('보안 승인여부', max_length=100, null=True,  choices=confirm_yn, default='0')
	prov_yn1_text = models.TextField('반려사유', blank=True, null=True, help_text="""반려 시 사유를 작성해주세요.""")
	prov_yn2 = models.CharField('성능 승인여부', max_length=100, null=True,  choices=confirm_yn, default='0')
	prov_yn2_text = models.TextField('성능Comment', blank=True, null=True, help_text="""반려 시 사유를 작성해주세요.""")
	prov_yn1_dtm = models.DateTimeField('보안 승인 일자', null=True)
	prov_yn2_dtm = models.DateTimeField('성능 승인 일자', null=True)
	privacy_yn = models.CharField('개인정보유무', max_length=100, null=True, choices=privacy_choice_yn, default='0', help_text="""개인정보를 조회하는 경우 보안센터 승인을 받은 후 수행할 수 있습니다.""")
	data_title = models.CharField('제목',max_length=1000, null=True, blank=True)
	data_explain = models.TextField('설명', null=True)
	sql_text = models.TextField('관련SQL',max_length=30000, null=True, blank=True, help_text="""":"로 바인딩하여 SQL을 작성하면 동적으로 파라메터 값을 받을 수 있습니다. 예를들면, :상픔코드, :주문일자 와 같이 바인딩 사용 시 사용자가 SQL을 실행할 때 상품코드와 주문일자를 입력할 수 있습니다.<br><font color="red"><b>in (:in_param) 으로 사용 시 멀티 값 입력 가능합니다.</b></font>주의: :yyyy :mm :dd :hh :mi :ss :digit 등은 바인드 변수로 사용할 수 없습니다.""")
	exp_order = models.IntegerField('화면노출순서', blank=True, null=True, default=99)
	exp_yn = models.CharField('노출여부', max_length=100, null=True, choices=choice_yn, default='0', help_text=""""Y" 상태이어야 다른 직원에게 공유됩니다.""")
	execute_cnt = models.IntegerField('수행횟수', blank=True, null=True, default=0)
	# id_req_user = models.ForeignKey(User, verbose_name='요청자', null=True, on_delete=models.PROTECT, related_name="User_DataList_req_user", db_column='id_req_user', blank=True)
	id_req_users = models.ManyToManyField(User, verbose_name='요청자 (복수 선택 가능)',  max_length=300,  blank=True, db_table = 'cust_datalist_user_id_req_users', related_name='cust_datalist_user_id_req_users', help_text="""해당 데이터를 조회할 수 있는 직원입니다.""")
	id_mod_psbl_users = models.ManyToManyField(User, verbose_name='수정자 (복수 선택 가능)',  max_length=300,  blank=True, db_table = 'cust_datalist_user_id_mod_psbl_users', related_name='cust_datalist_user_id_mod_psbl_users', help_text="""해당 데이터를 수정할 수 있는 직원입니다.""")
	realoretl = models.CharField('실시간or분석', max_length=100, null=True, choices=realoretl_yn, default=0)

	class Meta :
		verbose_name = '데이터 리스트'
		verbose_name_plural = '데이터 리스트'
		db_table = 'cust_data_list'

	def __str__(self) :
		return self.data_title


class DataRequest(models.Model) :
	confirm_yn = ( ('1','승인'),('0','승인대기'),('2','반려'))

	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_DataRequest_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_DataRequest_mod_user", db_column='id_mod_user', blank=True)
	id_datalist = models.ForeignKey(DataList, verbose_name='조회 데이터', null=True, on_delete=models.CASCADE, db_column='id_datalist', blank=True)
	data_title = models.CharField('제목',max_length=1000, null=True)
	data_explain = models.TextField('필요사유', null=True, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자',null=True, blank=True)
	prov_yn = models.CharField('검토여부', max_length=100, null=True, blank=True,  choices=confirm_yn, default='0')
	prov_yn_dtm = models.DateTimeField('검토일자', null=True)
	poss_view_dtm = models.DateTimeField('조회가능일자', null=True)
	id_prov_user = models.ForeignKey(User, verbose_name='검토자', null=True, on_delete=models.PROTECT, related_name="User_DataRequest_prov_user1", db_column='id_prov_user', blank=True)


	class Meta :
		verbose_name = '데이터 요청'
		verbose_name_plural = '데이터 요청'
		db_table = 'cust_data_request'

	def __str__(self) :
		return self.data_title

class BatchList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))


	alphanumeric = RegexValidator(r'^[a-zA-Z_]*$', '영문,언더바(_)만 입력 가능합니다.')

	batch_type = ( ('2','GSSHOP 사원 수집 배치'),('1','SmartDBA 내부 배치'),('0','Staging 배치'))

	batch_title = models.CharField('배치 제목',max_length=1000, default="None")
	batch_system_name = models.CharField('배치 영문명(알파벳+언더바만 가능)',max_length=1000, validators=[alphanumeric], default="None")
	target_table = models.CharField('대상 테이블',max_length=100, default="None")
	use_yn = models.CharField('사용여부', max_length=30, choices=choice_yn, default='0')
	truncate_yn = models.CharField('Truncate여부', max_length=30, choices=choice_yn, default='0')
	id_dbtype = models.ForeignKey(DbType, verbose_name='DBMS종류', null=True, on_delete=models.PROTECT, db_column='id_dbtype', blank=True)
	batch_type = models.CharField('배치구분', max_length=30, choices=batch_type, default='0')
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_BatchList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_BatchList_mod_user", db_column='id_mod_user', blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	sql_text = models.TextField('관련SQL',max_length=10000, default="SELECT 1 FROM DUAL")
	batch_order = models.IntegerField('배치구분 별 실행순서', default=100)

	class Meta :
		verbose_name = 'SmartDBA배치'
		verbose_name_plural = 'SmartDBA배치'
		db_table = 'cust_batch_list'



	def __str__(self) :
		return self.batch_title




class DatabaseMap(models.Model) :

	oper_type = (
					('0','도메인레벨'),
					('1','DB레벨'),
		)

	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도',        on_delete=models.PROTECT, db_column='id_dblist', blank=True,null=True)
	id_domain = models.ForeignKey(Domain, verbose_name='업무도메인명', on_delete=models.PROTECT, db_column='id_domain', blank=True,null=True)
	xy = models.CharField('좌표',  max_length=100, null=True, blank=True)
	map_type = models.CharField('구분',  max_length=100, choices=oper_type, null=True, blank=True);
	etc1 = models.CharField('기타',  max_length=100, null=True, blank=True)

	class Meta :
		verbose_name = '데이터베이스 지도 이미지 매핑 테이블'
		verbose_name_plural = '데이터베이스 지도 이미지 매핑 테이블'
		db_table = 'cust_database_map'

	def __str__(self) :
		return "{id_dblist} / {id_domain}".format(id_dblist=self.id_dblist.db_use,
												  id_domain=self.id_domain.domain_name,)

class TuningStatus(models.Model) :
	status = models.CharField('튜닝진행상태',max_length=100)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_TuningStatus_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_TuningStatus_mod_user", db_column='id_mod_user', blank=True)

	class Meta :
		verbose_name = '튜닝진행상태 (튜닝요청/튜닝완료/배포요청 등)'
		verbose_name_plural = '튜닝진행상태 (튜닝요청/튜닝완료/배포요청 등)'
		db_table = 'cust_tuning_status'

	def __str__(self) :
		return self.status

class ProjectList(models.Model) :
	start_dtm = models.DateField('프로젝트 시작 일자')
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, db_column='id_reg_user', blank=True)
	title = models.CharField('프로젝트명',max_length=100)

	class Meta :
		verbose_name = '프로젝트 리스트'
		verbose_name_plural = '프로젝트 리스트'
		db_table = 'cust_project_list'

	def __str__(self) :
		return self.title

class MetaGrantList(models.Model) :
	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.CASCADE, db_column='id_dblist', blank=True,null=True)
	app_service = models.CharField('API(서비스)',max_length=100, blank=True, null=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.SET_NULL, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = '테이블 권한 : DB<->API(서비스) 매핑'
		verbose_name_plural = '테이블 권한 : DB<->API(서비스) 매핑'
		db_table = 'cust_meta_grant_list'
		ordering = ('app_service',)

	def __str__(self) :
		return self.app_service

class MetaGrantDetail(models.Model) :
	id_metagrantlist = models.ForeignKey(MetaGrantList, verbose_name='API(서비스)', on_delete=models.CASCADE, db_column='id_metagrantlist', blank=True,null=True)
	role = models.CharField('GRANTEE',max_length=100, blank=True, null=True)
	crud = models.CharField('CRUD',max_length=100, blank=True, null=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.SET_NULL, db_column='id_reg_user', blank=True)

	class Meta :
		verbose_name = '테이블 권한 : API(서비스)<->권한 매핑'
		verbose_name_plural = '테이블 권한 : API(서비스)<->권한 매핑'
		db_table = 'cust_meta_grant_detail'

	def __str__(self) :
		return self.id_metagrantlist.app_service

class TuningList(models.Model) :

	sql_type = (    ('1','운영-온라인/신규'),
					('2','운영-온라인/변경'),
					('3','운영-배치/신규'),
					('4','운영-배치/변경'),
					('5','분석-신규'),
					('6','분석-배치'),
					('7','기타'),
				)
	title = models.CharField('제목', max_length=1000, null=True)
	sql_id = models.CharField('SQL_ID', max_length=1000, null=True)
	sql_type = models.CharField('신규or변경', max_length=30, choices=sql_type, default='0')
	id_domain = models.ForeignKey(Domain, verbose_name='업무도메인명', on_delete=models.PROTECT, db_column='id_domain', null=True, blank=True, default=3)
	id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', null=True, on_delete=models.PROTECT, db_column='id_dblist', to_field='id', blank=True, default=10)
	id_datalist = models.ForeignKey(DataList, verbose_name='DataList', null=True, on_delete=models.CASCADE, db_column='id_datalist', blank=True)
	id_projectlist = models.ForeignKey(ProjectList, verbose_name='프로젝트리스트', null=True, on_delete=models.CASCADE, db_column='id_projectlist', blank=True)
	id_tuningstatus = models.ForeignKey(TuningStatus, verbose_name='튜닝진행상태', on_delete=models.PROTECT, db_column='id_tuningstatus',  null=True, blank=True, default="1")
	sql_info = models.TextField('SQL 설명', null=True)
	tuning_info = models.TextField('튜너의견(튜너 작성)',null=True, blank=True)
	asis_plan = models.TextField('튜닝전	Plan(튜너 작성)',null=True, blank=True)
	tobe_plan = models.TextField('튜닝후 Plan(튜너 작성)',null=True, blank=True)
	asis_sql_text = models.TextField('튜닝전SQL',null=True, blank=True)
	asis_elapsed_time = models.FloatField('튜닝 전 응답 시간(초)', null=True)
	expect_elapsed_time = models.FloatField('튜닝 후 기대 응답 시간(초)', null=True)
	avg_rows = models.IntegerField('평균 결과 건수', null=True)
	daily_exec_cnt = models.IntegerField('일 실행 횟수', null=True)
	bind_value = models.TextField('바인딩값', null=True, blank=True, help_text="""SQL에 바인딩되는 값을 꼭 입력해주세요""")
	tobe_sql_text = models.TextField('튜닝후SQL(튜너 작성)',null=True, blank=True)
	tobe_elapsed_time = models.FloatField('튜닝 후 수행 시간', null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_TuningList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_TuningList_mod_user", db_column='id_mod_user', blank=True)
	id_tuning_user = models.ForeignKey(User, verbose_name='튜너', null=True, on_delete=models.PROTECT, related_name="User_TuningList_tuning_user", db_column='id_tuning_user', blank=True)
	tuning_dtm = models.DateTimeField('튜닝일자', null=True, blank=True)
	dist_dtm = models.DateTimeField('배포일자', null=True)
	reg_dtm = models.DateTimeField('등록일자')
	mod_dtm = models.DateTimeField('수정일자', null=True, blank=True)

	class Meta :
		verbose_name = '튜닝요청'
		verbose_name_plural = '튜닝요청'
		db_table = 'cust_tuning_list'

	def __str__(self) :
		return self.title


class ProcessList(models.Model) :

	process_nm = models.CharField('프로세스명',max_length=100)
	ordering = models.IntegerField('순서', blank=True, null=True, default=0)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_ProcessList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_ProcessList_mod_user", db_column='id_mod_user', blank=True)


	class Meta :
		verbose_name = '고객 행동 프로세스 (앱실행/주문완료...)'
		verbose_name_plural = '고객 행동 프로세스 (앱실행/주문완료...)'
		db_table = 'cust_process_list'

	def __str__(self) :
		return self.process_nm











class MenuList(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	menu_name = models.CharField('메뉴명', max_length=100, null=True, blank=True)
	menu_explain = models.CharField('비고', max_length=100, null=True, blank=True)
	default_permission_yn = models.CharField('기본권한', null=True, blank=True, max_length=30, choices=choice_yn, default='0')
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_MenuList_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_MenuList_mod_user", db_column='id_mod_user', blank=True)
	reg_dtm = models.DateTimeField('일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)
	use_yn = models.CharField('사용여부', null=True, blank=True, max_length=30, choices=choice_yn, default='1')
	url = models.CharField('URL', max_length=100, null=True, blank=True)


	class Meta :
		verbose_name = '메뉴분류'
		verbose_name_plural = '메뉴분류'
		db_table = 'cust_menu_list'

	def __str__(self) :
		return self.menu_name

class MenuPermission(models.Model) :

	id_menulist = models.ForeignKey(MenuList, verbose_name='메뉴명', null=True, on_delete=models.PROTECT, db_column='id_menulist', blank=True)
	id_grantee_user = models.ForeignKey(User, verbose_name='GRANTEE', null=True, on_delete=models.PROTECT, related_name="User_MenuPermission_grantee_user", db_column='id_grantee_user', blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, related_name="User_MenuPermission_reg_user", db_column='id_reg_user', blank=True)
	id_mod_user = models.ForeignKey(User, verbose_name='수정자', null=True, on_delete=models.PROTECT, related_name="User_MenuPermission_mod_user", db_column='id_mod_user', blank=True)
	reg_dtm = models.DateTimeField('일자', auto_now_add=True)
	mod_dtm = models.DateTimeField('수정일자', auto_now=True)

	class Meta :
		verbose_name = '메뉴사용자권한'
		verbose_name_plural = '메뉴사용자권한'
		db_table = 'cust_menu_permission'

	def __str__(self) :
		return self.id_grantee_user.first_name + "(" + self.id_grantee_user.last_name + ")" + " :: " + self.id_menulist.menu_name




class UserVisit(models.Model) :

	name = models.CharField('이름', max_length=100, null=True, blank=True)
	sabun = models.CharField('사번', max_length=100, null=True, blank=True)
	team_name = models.CharField('팀명', max_length=100, null=True, blank=True)
	id_menulist = models.ForeignKey(MenuList, verbose_name='메뉴리스트', null=True, on_delete=models.CASCADE, db_column='id_menulist', blank=True)
	reg_dtm = models.DateTimeField('일자', auto_now_add=True)

	class Meta :
		verbose_name = '사용자방문이력'
		verbose_name_plural = '사용자방문이력'
		db_table = 'cust_user_visit'

	def __str__(self) :
		return self.name


class UserRequestData(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	data_name = models.CharField('용어명',max_length=100,null=True, blank=True)
	data_text = models.TextField('요청내용',max_length=10000, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	complete_yn = models.CharField('완료여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0')


	class Meta :
		verbose_name = '사용자 데이터 요청'
		verbose_name_plural = '사용자 데이터 요청'
		db_table = 'cust_user_request_data'

	def __str__(self) :
		return self.data_name






class UserRequestWord(models.Model) :

	choice_yn = ( ('1','Y'),('0','N'))

	word_name = models.CharField('용어명',max_length=100,null=True, blank=True)
	word_text = models.TextField('요청내용',max_length=10000, null=True, blank=True)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	complete_yn = models.CharField('완료여부', null=True, blank=True, max_length=30, choices=choice_yn, default='0')

	class Meta :
		verbose_name = '사용자 데이터 요청'
		verbose_name_plural = '사용자 데이터 요청'
		db_table = 'cust_user_request_word'

	def __str__(self) :
		return self.word_name






class UserSearchKeyword(models.Model) :

	keyword = models.CharField('검색어',max_length=100)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)

	class Meta :
		verbose_name = '사용자 검색키워드'
		verbose_name_plural = '사용자 검색키워드'
		db_table = 'cust_user_search_keyword'

	def __str__(self) :
		return self.keyword

class UserClickData(models.Model) :

	data = models.CharField('데이터',max_length=100)
	id_data = models.IntegerField('데이터번호', default=0)
	data_type = models.IntegerField('데이터타입', default=0)
	id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.PROTECT, blank=True)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)

	class Meta :
		verbose_name = '사용자 클릭데이터'
		verbose_name_plural = '사용자 클릭데이터'
		db_table = 'cust_user_click_data'

	def __str__(self) :
		return self.data

class UserExecuteSQL(models.Model) :

	sql_text = models.TextField('관련SQL', default="SELECT 1 FROM DUAL")
	id_reg_user = models.TextField('수행자',max_length=1000)
	reg_dtm = models.DateTimeField('등록일자', auto_now_add=True)
	execute_time = models.FloatField('수행시간', blank=True, null=True)
	id_datalist = models.CharField('데이터리스트', max_length=100, blank=True,null=True)
	id_dbdetail = models.ForeignKey(DbDetail, verbose_name='DB상세', null=True, on_delete=models.CASCADE, blank=True)

	class Meta :
		verbose_name = '사용자 실행SQL 이력'
		verbose_name_plural = '사용자 실행SQL 이력'
		db_table = 'cust_user_execute_sql'

class WeekDBA(models.Model) :

	choice_yn = ( ('22980','이치호'),
				  ('22764','이정아'),
				  ('22917','정관호'),
				  ('D4563','김진석'),
				)

	freezing_yn = ( ('1','Freezing'),('0','운영 반영 신청가능'))

	dba = models.CharField('DBA', null=True, blank=True, max_length=30, choices=choice_yn)
	dist_dtm = models.DateTimeField('정기반영일자',null=True, blank=True)	

	class Meta :
		verbose_name = '금주DBA'
		verbose_name_plural = '금주DBA'
		db_table = 'cust_week_dba'

	def __str__(self) :
		return self.dba



class DataDocumentPRD(ColumnList):
    class Meta:
        proxy = True
        verbose_name = '[데이터문서화-상품] 상품 데이터 문서화'
        verbose_name_plural = '[데이터문서화-상품] 상품 데이터 문서화'

class SecureApprove(DataList):
    class Meta:
        proxy = True
        verbose_name = '[DataList] 보안센터-데이터노출승인'
        verbose_name_plural = '[DataList] 보안센터-데이터노출승인'

class DataModel(models.Model):
    id_dblist = models.ForeignKey(DbList, verbose_name='DB용도', on_delete=models.CASCADE, db_column='id_dblist', blank=True, null=True)
    id_domainanddblist = models.ForeignKey(DomainAndDbList, verbose_name='도메인명', on_delete=models.SET_NULL, db_column='id_domainanddblist', blank=True, null=True)
    title = models.CharField('도메인', max_length=200, null=True, blank=True, help_text="상세 도메인이 없는 경우 DB용도와 동일 값 입력")
    file = models.FileField('모델업로드',null=True, validators=[validate_file_extension],help_text="반드시 물리 모델 업로드, 논리 모델은 안됨")        
    reg_dtm = models.DateTimeField('등록일자', auto_now_add=True, null=True, blank=True)
    mod_dtm = models.DateTimeField('수정일자', auto_now=True, null=True, blank=True)
    id_reg_user = models.ForeignKey(User, verbose_name='등록자', null=True, on_delete=models.DO_NOTHING, db_column='id_reg_user', blank=True)
    remarks = models.CharField('비고',max_length=1000, default='', null=True, blank=True)
    exp_order = models.IntegerField('DB 별 화면노출순서', blank=True, null=True, default=99, help_text="같은 DB 내 도메인 노출 순서")
    

    def clean(self):
        
        try :        	        	
	        f = self.file

	        html = f.read()

	        filename = f.file.name
	        
	        lFile_name = (filename).split('.')

	        html = self.file.open(self)
	        html = html.read().decode('utf8')

	        if html.find('물리ERD전환') > 0 :
	        	return
        except :
        	return

        dict_tab = {}
        dict_col = {}

        v_db = self.id_domainanddblist.id_dblist.db_use
        v_domain = self.id_domainanddblist.id_domain.domain_name
        v_title = v_db + "(" + v_domain + ")"

        # 테이블 상세 정보 삭제
        p = re.compile("<div class='card'.+", re.DOTALL)
        html = p.sub('', html)        
        
        # 제목 변경
        p = re.compile("(<html.+?<title>)(.+?)(</title>)", re.DOTALL)
        html = p.sub('\g<1>' +  v_title + ' 데이터 모델' + '\g<3>', html)        
        
        p = re.compile('(<a name=.+?><h4>)(.+?)(</h4>)', re.DOTALL)        
        html = p.sub('\g<1>' +  v_title + ' 데이터 모델' + '\g<3>', html)        
        
        # Master 테이블에 붉은색 처리
        p = re.compile("<linearGradient.+?</linearGradient>",re.DOTALL|re.IGNORECASE)
        lineargradient = """
        <lineargradient id="tbg_C13939" x1="0%" y1="0%" x2="0%" y2="100%">
           <stop offset="0%" stop-color="#FFD4D4"></stop> 
           <stop offset="80%" stop-color="#CDB4B4"></stop> 
           <stop offset="100%" stop-color="#CDB4B4"></stop> 
        </lineargradient>

        """
        m = p.findall(html)
        for n in m :        	
        	html = html.replace(n, n + lineargradient)
        	break        
        
        p = re.compile("(<path.+?url\(#tbg_)(.+?)(\).+?>\n<rect.+?>\n.+?<text.+?>.+?_M</text>)", re.I)
        html = p.sub('\g<1>C13939\g<3>', html)

        # TABLE 치환
        # p = re.compile("(<text.+?>)(.+?)(</text><title>Table.+?\.)(.+?)(\n)(.+?)(</title>)")
        p = re.compile("(<text.+?)(>)(.+?)(</text>)(<title>Table.+?\.)(.+?)(\n)(.+?)(</title>)")

        m = p.findall(html)
        for n in m:
            dict_tab[n[2].replace(' ','')] = n[7].replace(' ','')

        m = p.findall(html)
        for n in m:
            dict_tab[n[2].replace(' ','')] = n[7].replace(' ','')

        # html = p.sub('\g<1>\g<6>\g<3>\g<4>\g<5>\g<6>\g<7>', html)
        html = p.sub('\g<1> model="p" style="display: none" \g<2>\g<3>\g<4>' +
                     '\g<1> model="l"                       \g<2>\g<8>\g<4>' +
                     '\g<5>\g<6>\g<7>\g<8>\g<9>'
                     , html)

        # 컬럼 치환
        # p = re.compile("(<text id='.+?\..+?\..+?'.+?>)(.+?)(</text><title>)(.+?)(\n.+?\n)(.+?)(</title>)")
        p = re.compile("(<text id='.+?\..+?\..+?'.+?)(>)(.+?)(</text>)(<title>)(.+?)(\n.+?\n)(.+?)(</title>)")

        m = p.findall(html)
        for n in m:
            dict_col[n[2].replace(' ','')] = n[7].replace(' ','')

        # html = p.sub('\g<1>\g<6>\g<3>\g<4>\g<5>\g<6>\g<7>', html)        
        # html = p.sub('\g<1> model="p" style="display: none" \g<2>\g<3>\g<4>' +
        #              '\g<1> model="l"                       \g<2>\g<8>\g<4>' +
        #              '\g<5>\g<6>\g<7>\g<8>\g<9>'
        #              , html)

        html = p.sub('\g<1>\g<2><a model="p" style="display: none">\g<3></a><a model="l">\g<8></a>\g<4>\g<5>\g<6>\g<7>\g<8>\g<9>', html)

        # fk명 제거
        p = re.compile("(<title>)(Fk FK.+?)(\n)")
        html = p.sub('\g<1>\g<3>', html)

        # 광고 제거
        p = re.compile("(class='legendTitle'.+?>)(.+?)(</text>)(.+?\n.+?)(<a.+?</a>)(.+?\n.+?<tspan>)(.+?)(</tspan>)")
        html = p.sub('\g<1>단축키\g<3>\g<4>\g<6>물리ERD전환 : P / 논리ERD전환 : L\g<8>', html)

        
        p = re.compile("(<text x='.+?' y='.+?' transform='rotate\(.+?\)' class='relName'>)(.+?)(</text>)")
        m = p.findall(html)
        for n in m :
        	eng_relName = n[1] 
        	l_eng_relName = eng_relName.split(',') 
        	l_kor_relName = [] 
        	for l in l_eng_relName: 
        		try: 
        			l_kor_relName.append(dict_col[l]) 
        		except Exception: 
        			l_kor_relName.append(l)

			
            # print(eng_columns)
            # print(kor_columns)
            # print()
            
        	kor_relName = ','.join(l_kor_relName)
        	imsi_p = re.compile("(<text x='.+?' y='.+?' transform='rotate\(.+?\)' class=)('relName'>)("+eng_relName+")(</text>)")
        	html = imsi_p.sub("\g<1>"+"'relName' model='p' style='display: none'>" + eng_relName + "\g<4>" +\
        		              "\g<1>"+"'relName' model='l'                      >" + kor_relName + "\g<4>", html)




        # fk 컬럼 논리명으로 치환
        p = re.compile("(<title>\n)(.+?)( ref )(.+?)( \( )(.+?)( \)</title>)")

        m = p.findall(html)
        for n in m:
            from_eng_table = n[1]
            to_eng_table = n[3]

            from_eng_table = from_eng_table.replace(' ','')
            to_eng_table = to_eng_table.replace(' ','')

            from_kor_table = dict_tab[from_eng_table]
            to_kor_table = dict_tab[to_eng_table]


            eng_columns = n[5]

            l_eng_columns = eng_columns.split(' ')
            l_kor_columns = []
            for l in l_eng_columns:
                try:
                    if l.find(",") > 0:
                        l_kor_columns.append(dict_col[l.replace(",", "")] + ",")
                    else:
                        l_kor_columns.append(dict_col[l])
                except Exception:
                    l_kor_columns.append(l)

            kor_columns = ' '.join(l_kor_columns)
            # print(eng_columns)
            # print(kor_columns)
            # print()

            imsi_p = re.compile("(<title>\n.+? ref .+? \( )(" + eng_columns + ")( \)</title>)")
            html = imsi_p.sub('\g<1>' + kor_columns + '\g<3>', html)

            imsi_p = re.compile("(<title>\n)(.+?)( ref )(.+?)( \( )(.+?)( \)</title>)")
            html = imsi_p.sub('\g<1>' + from_kor_table + '\g<3>' + to_kor_table + '\g<5>\g<6>\g<7>', html)

        html = html + "\n" + \
        """
        <script src="https://code.jquery.com/jquery-latest.min.js"></script>
        <script>
            document.onkeyup = function(e) {
                if (e.which == 80 ) {
                    $('text[model="l"]').css('display','none');
                    $('text[model="p"]').css('display','block');
                    $('a[model="l"]').css('display','none');
                    $('a[model="p"]').css('display','block');
                }
                if (e.which == 76 ) {
                    $('text[model="l"]').css('display','block');
                    $('text[model="p"]').css('display','none');
                    $('a[model="l"]').css('display','block');
                    $('a[model="p"]').css('display','none');
                }
            }       
        </script>
        """
        
        
        print(f)
        f.truncate(0)
        f.write(html.encode('utf-8'))        


    class Meta :
    	verbose_name = '데이터모델'
    	verbose_name_plural = '데이터모델'
    	db_table = 'cust_data_model'



# class RegisterData(DataList):
#     class Meta:
#         proxy = True
#         verbose_name = '[DataList] DevOps-데이터 생성'
#         verbose_name_plural = '[DataList] DevOps-데이터 생성'