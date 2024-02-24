# post_extras.py
from django import template
from database.models import *
from database.views import *

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
      # dataset = [{'EMP_NM':'?','NAME':'?','MOBILE':'?','SUB_MAIL':'?'}]
      dataset = []

    return dataset

register = template.Library()

@register.simple_tag
def get_it_manager(id_dblist, id_domain):

	obj = DomainAndDbList.objects.filter(id_dblist=id_dblist,
										 id_domain=id_domain,)

	if obj :
		obj = obj[0]
		return ", ".join([p.first_name + "(" + p.last_name + ")"  for p in obj.it_manager.all()])
	else :
		return ""

@register.simple_tag
def get_add_privacy_yn(id_metareq):

	add_secu_yn = ""

	metareqlist = MetaReqList.objects.filter(id_metareq=id_metareq)

	for m in metareqlist :
		if m.privacy_list != "0" and m.change_list in ['+ 신규','+ └ TOBE'] :
		  add_secu_yn = "Y"
		  break

	return add_secu_yn

@register.simple_tag
def get_replace_br(val):
	if val :
		return val.replace("</p><p>","<br>")
	else :
		return ""


@register.simple_tag
def get_dba():
	obj = WeekDBA.objects.all().first()
	username = User.objects.filter(username=obj.dba).first()
	return username

@register.simple_tag
def get_dist_dtm():
	obj = WeekDBA.objects.all().first()
	return obj.dist_dtm



@register.simple_tag
def get_dev_manager(id_dblist, id_domain):

	obj = DomainAndDbList.objects.filter(id_dblist=id_dblist,
										 id_domain=id_domain,)


	if obj :
		obj = obj[0]
		return ", ".join([p.first_name + "(" + p.last_name + ")"  for p in obj.dev_manager.all()])
	else :
		return ""

@register.simple_tag
def get_passwd(sabun):

	# 패스워드 같은 로직으로 생성
	cal = 0
	for c in sabun :
	  if c.isalpha() :
	    c = ord(c)

	  cal = cal + int(c)*111


	v1 = "gsshop"
	v2 = str(cal%1000)

	passwd = v1+"_"+v2

	return passwd

@register.simple_tag
def get_crud(user_id, id_dblist,oper_cd,owner,table_name):

	username = ""


	sql = """
	  select id, username
	  from cust_user_list
	  where id_user_name = {user_id}
	    and id_dblist = {id_dblist};
	""".format(user_id=user_id,
	           id_dblist=id_dblist)

	ds = _query_dict("default",sql)


	if len(ds) == 0 :
	  return ""

	else :
	  ds = ds[0]
	  username = ds['username']

	sql = """
	  SELECT distinct privilege
	  FROM STG_DBA_TAB_PRIVS A
	  WHERE A.ID_DBLIST = {id_dblist}
	    AND A.OPER_CD = {oper_cd}
	    AND A.OWNER = '{owner}'
	    AND A.TABLE_NAME = '{table_name}'
	    AND A.GRANTEE = '{username}'
	  ORDER BY CASE WHEN privilege = 'INSERT' then 1
	  				WHEN privilege = 'SELECT' THEN 2
	  				WHEN privilege = 'UPDATE' THEN 3
	  				WHEN privilege = 'DELETE' THEN 4
	  				ELSE 5 END
	""".format(
	            id_dblist=id_dblist,
	            oper_cd=oper_cd,
	            owner=owner,
	            table_name=table_name,
	            username=username,
	          )


	ds = _query_dict("default",sql)

	crud = ""

	for d in ds :
		if d['privilege'] == "INSERT" :
			crud += "C"
		elif d['privilege'] == "UPDATE" :
			crud += "U"
		elif d['privilege'] == "DELETE" :
			crud += "D"
		elif d['privilege'] == "EXECUTE" :
			crud += "EXECUTE"

	return crud

@register.simple_tag
def f_get_datatype(id_stdattr,db_type) :

	data = StdAttr.objects.get(id=id_stdattr)

	in_data_type = ""

	if data :

		if db_type == "ORACLE" :
			in_data_type = data.id_stddomain.oracle_datatype


		elif db_type in ("MYSQL","MARIADB") :
		    in_data_type = data.id_stddomain.mysql_datatype

	return in_data_type


@register.simple_tag
def get_stdword(kor_attr, eng_attr, data_type, db_type):

	eng_attr = eng_attr.upper()
	data_type = data_type.upper()
	error_message = ""
	std_yn = "비표준"

	dataset_yn = StdAttr.objects.filter(std_attr_eng__iexact=eng_attr,
                                        std_attr_kor__iexact=kor_attr,
                                        accept_yn=0,
                                        use_yn=1).exists()

	if dataset_yn == True :
		dataset = StdAttr.objects.filter( std_attr_eng__iexact=eng_attr,
                                        std_attr_kor__iexact=kor_attr,
                                        accept_yn=0,
                                        use_yn=1)

		for in_data in dataset :
			if db_type == "ORACLE" :
				if ( data_type.upper() == (in_data.id_stddomain.oracle_datatype).upper() ) :
				  std_yn = "표준"
			elif db_type in ("MYSQL","MARIADB") :
				if ( data_type.upper() == (in_data.id_stddomain.mysql_datatype).upper() ) :
				  std_yn = "표준"

	return std_yn

