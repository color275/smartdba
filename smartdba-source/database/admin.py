
from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Q

from django_summernote.admin import SummernoteModelAdmin
from django_summernote.admin import SummernoteInlineModelAdmin
import datetime
import time

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from django.utils.html import format_html

# admin.site.register(TableList)
# admin.site.register(DomainList)
# admin.site.register(ColumnList)
# admin.site.register(DbList)


class DataModelAdmin(admin.ModelAdmin):

	# list_display_links = ('std_wd_kor',)
	# search_fields = ('=std_wd_kor',)

	autocomplete_fields =('id_domainanddblist',)
	list_editable = ('exp_order',)
	fields = (		
		'id_domainanddblist',		
		'file',
		'exp_order',
		'remarks',
		)
	list_display = (
		'id_domainanddblist',		
		'exp_order',
		'reg_dtm',
		'mod_dtm',
		'id_reg_user',
		'remarks',
		)
	ordering = ('id_domainanddblist__id_dblist__exp_order','exp_order')
	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

admin.site.register(DataModel, DataModelAdmin)


class StdWordAdmin(admin.ModelAdmin):

	list_display_links = ('std_wd_kor',)
	search_fields = ('=std_wd_kor',)

	fields = (
		'std_wd_kor',
		'std_wd_eng',
		'std_wd_eng_ful',
		'expl',
		'accept_yn',
		'reject_exp',
		)
	list_display = (
		'std_wd_kor',
		'std_wd_eng',
		'std_wd_eng_ful',
		'reg_dtm',
		'id_reg_user',
		'expl',
		'accept_yn',
		'reject_exp',
		)
	def save_model(self, request, obj, form, change):
		if change :
			pass
		else :
			obj.id_reg_user = request.user
		obj.save()

admin.site.register(StdWord, StdWordAdmin)

class StdDomainAdmin(admin.ModelAdmin):

	list_display_links = ('domain_name',)

	search_fields = ('=domain_name','info_type')

	fields = (
		'id_stddatatype',
		'id_std_domaintype',
		'domain_name',
    'group_code_yn',
    'group_code',
		'info_type',
		'oracle_datatype',
		'mysql_datatype',
		'expl',
		'accept_yn',
		'reject_exp',
		'use_yn',
		)
	list_display = (
		'id_stddatatype',
		'id_std_domaintype',
		'domain_name',
    'group_code_yn',
    'group_code',
		'info_type',
		'oracle_datatype',
		'mysql_datatype',
		'accept_yn',
		'reject_exp',
		'reg_dtm',
		'mod_dtm',
		'id_reg_user',
		'use_yn',
		)
	ordering = ('-reg_dtm',)

	def save_model(self, request, obj, form, change):		
		if change :
			pass
		else :
			obj.id_reg_user = request.user
		obj.save()

admin.site.register(StdDomain, StdDomainAdmin)

class StdAttrAdmin(admin.ModelAdmin):

	autocomplete_fields =('id_stddomain',)

	list_editable = ('accept_yn',)

	list_display_links = ('std_attr_kor',)

	search_fields = ('=std_attr_kor',)

	fields = (
		'id_stddomain',
		'std_attr_kor',
		'std_attr_eng',
		'csr_no',
		'accept_yn',
		'reject_exp',
		'use_yn',
		)
	list_display = (
		'std_attr_kor',
		'std_attr_eng',
		'id_stddomain',
		'csr_no',
		'accept_yn',
		'expl',
		'reject_exp',
		'reg_dtm',
		'mod_dtm',
		'id_reg_user',
		'use_yn',
		)
	def save_model(self, request, obj, form, change):		
		if change :
			pass
		else :
			obj.id_reg_user = request.user
		obj.save()

admin.site.register(StdAttr, StdAttrAdmin)

class StdDataTypeAdmin(admin.ModelAdmin):



	fields = (
		'data_typ_nm',
		)
	list_display = (
		'id',
		'data_typ_nm',
		)

admin.site.register(StdDataType, StdDataTypeAdmin)

class WeekDBAAdmin(admin.ModelAdmin):



	list_display = (
		'id',		
		'dba',
		'dist_dtm',
		)
	list_editable = (		
		'dba',
		'dist_dtm',
		)

admin.site.register(WeekDBA, WeekDBAAdmin)

class OperCdAdmin(admin.ModelAdmin):



	list_display = (
		'id',
		'oper_cd',
		)

	list_per_page = 30

admin.site.register(OperCd, OperCdAdmin)

class DBOwnerAdmin(admin.ModelAdmin):

	autocomplete_fields =('id_dblist',)

	list_display = (
		'id_dblist',
		'owner',
		)
	ordering = (
		'id_dblist__db_use',
		)

	search_fields = (
		'id_dblist__db_use',
		)

	list_per_page = 30

admin.site.register(DBOwner, DBOwnerAdmin)



class DomainAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''

	# autocomplete_fields =('it_manager','dev_manager')

	list_display_links = ('domain_name',)

	list_display = (
		'domain_name',
		'id',
		# 'get_it_manager',
		# 'get_dev_manager',
		)
	ordering = (
		'-reg_dtm',
		)
	search_fields = (
		'domain_name',
		)

	list_per_page = 100

	ordering = ['domain_name',]



admin.site.register(Domain, DomainAdmin)

class ChannelAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display_links = (
		'channel_name',
		)
	list_display = (
		'channel_name',
		'exp_order',
		)
	list_editable = (
		'exp_order',
		)

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()


admin.site.register(Channel, ChannelAdmin)

class DataTypeAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''

	list_display_links = (
		'data_type',
		)
	list_display = (
		'data_type',
		'exp_order',
		)
	fields = (
		'data_type',
		'exp_order',
		)
	# list_editable = (
	# 	'channel_type',
	# 	'DataType_name',
	# 	)
	search_fields = (
		'data_type',
		)
	list_filter = (
		'data_type',
		)
	list_editable = (
		'exp_order',)
	list_per_page = 30

	list_display_links = ('data_type',)



	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()


admin.site.register(DataType, DataTypeAdmin)

class DbListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''

	autocomplete_fields =('id_manager',)

	list_display_links = (
		'db_use',
		)

	# list_display = [field.name for field in DbList._meta.fields if field.name not in ["reg_dtm","mod_dtm","db_desc","eos_explain","map_coords"] ]
	list_display = [
		'db_use',
		'use_yn',
		# 'monitor_yn',
		'infra_op_yn',
		'metareq_yn',
		'gather_meta_yn',
		'privacy_yn',
		'emp_privacy_yn',
		'exp_order',
		'id_manager',
		'id_channel',
		'id_dbtype',
		'id_dbposition',
		'db_ver',
		'eos_yn',
		'eos_dt',
	]
	search_fields = (
		'db_use',
		)
	# list_editable = [field.name for field in DbList._meta.fields if field.name not in ["id","db_use","reg_dtm","mod_dtm","db_desc","eos_explain"] ]
	list_editable = ['infra_op_yn','privacy_yn','emp_privacy_yn','use_yn','gather_meta_yn','metareq_yn','id_dbtype']
	# list_editable = ['metareq_yn','eos_dt','infra_op_yn','exp_order','monitor_yn'	]
	ordering = (
		'exp_order',
		)
	list_filter = (
		'id_dbtype','eos_yn','privacy_yn','use_yn'
		)
	list_per_page = 100

	# def get_queryset(self, request):
	# 	qs = super().get_queryset(request)
	# 	return qs.filter(oper_cd="운영")


admin.site.register(DbList, DbListAdmin)

class DbAdmin(admin.ModelAdmin):
	
	list_display = [field.name for field in Db._meta.fields if field.name not in ["id",]]

	fields = [field.name for field in Db._meta.fields if field.name not in ["id","id_reg_user","reg_dtm","id_mod_user","mod_dtm"] ]

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		obj.id_mod_user = request.user
		obj.save()

	ordering = ['db_type',]


admin.site.register(Db, DbAdmin)

class DbTypeAdmin(admin.ModelAdmin):
	
	list_display = [field.name for field in DbType._meta.fields if field.name not in ["id","db_type"]]


	# list_editable = [field.name for field in DbType._meta.fields if field.name not in ["id","id_reg_user","reg_dtm"] ]
	fields = [field.name for field in DbType._meta.fields if field.name not in ["id","id_reg_user","reg_dtm","db_type"] ]

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

	ordering = ['id_db__db_type','-version']


admin.site.register(DbType, DbTypeAdmin)


class DbPositionAdmin(admin.ModelAdmin):


	list_display = [field.name for field in DbPosition._meta.fields]


	list_editable = [field.name for field in DbPosition._meta.fields if field.name not in ["id","id_reg_user","reg_dtm"] ]
	fields = [field.name for field in DbPosition._meta.fields if field.name not in ["id","id_reg_user","reg_dtm"] ]

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

admin.site.register(DbPosition, DbPositionAdmin)		

class DBTablespaceAdmin(admin.ModelAdmin):

	autocomplete_fields =(
		'id_dblist',)


	list_display = [
		'id_owner',
		'id_dblist',
		'tablespace_name',
	]



	fields = [
		'id_owner',
		'id_dblist',
		'tablespace_name',
	]

	search_fields = ['id_dblist__db_use',]

	ordering = ['id_owner__owner',]

admin.site.register(DBTablespace, DBTablespaceAdmin)






class HaCaseAdmin(admin.ModelAdmin):


	list_display = [
	    'id',
		'ha_case',
		'reg_dtm',
		'id_reg_user'
	]

	fields = ['ha_case',]

	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

admin.site.register(HaCase, HaCaseAdmin)

# class DBDetailMonitorItemListAdmin(admin.TabularInline):
#     model = DBDetailMonitorItemList
#     extra = 0

#     fields = [
# 	'id_dbdetail',
# 	'id_monitoritemlist',
# 	'risk_level',
# 	'compare_case',
# 	'limit_value',
# 	]

# admin.site.register(DBDetailMonitorItemList)

# class DBDetailMonitorItemListAdmin(admin.ModelAdmin):

# 	autocomplete_fields =('id_dbdetail','id_monitoritemlist',)

# 	fields = [
# 		'id_dbdetail',
# 		'id_monitoritemlist',
# 		'limit_value',
# 		'risk_level',
# 	]


# 	def save_model(self, request, obj, form, change):
# 		obj.id_reg_user = request.user
# 		obj.save()

# admin.site.register(DBDetailMonitorItemList, DBDetailMonitorItemListAdmin)


class DbDetailAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs	'''
	
	autocomplete_fields =('id_dblist','id_sms_receive_user',)

	# inlines = (DBDetailMonitorItemListAdmin,)

	list_editable = ('use_yn','id_hacase','alert_yn','db_order',)

	list_display_links = (
		'__str__',
		)

	# fields = [field.name for field in DbDetail._meta.fields if field.name not in ["reg_dtm","mod_dtm","tns_desc"] ]

	list_display = [
		'__str__',
		'id',
		'use_yn',		
		'alert_yn',
		'id_hacase',
		'db_order',
		'host_nm',
		'db_nm',
		'inst_nm',
		'svr_ip',
		'svc_ip',
		'port',
	]

	search_fields = (
		'id_dblist__db_use',
		'host_nm',
		'svr_ip',
		'svc_ip',
		)
	ordering = (
		'id_dblist__exp_order',
		'id_dblist__db_use',
		'-oper_cd',
		'db_order',

		)
	list_filter = (
		'use_yn','alert_yn','oper_cd','id_dblist__db_use'
		)
	list_per_page = 1000

	actions = ['update_alert_y','update_alert_n',]

	def update_alert_y(self, request, queryset):
		queryset.update(alert_yn='1')
	update_alert_y.short_description = """선택된 항목에 대해 ALERT 여부를 "Y"로 변경합니다. """

	def update_alert_n(self, request, queryset):
		queryset.update(alert_yn='0')
	update_alert_n.short_description = """선택된 항목에 대해 ALERT 여부를 "N"로 변경합니다. """

	# def save_model(self, request, obj, form, change):
		
	# 	obj.save()

	# 	if change :
	# 		return
		
	# 	id_dbtype = obj.id_dblist.id_dbtype
	# 	id_hacase = obj.id_hacase

	# 	monitoritemlist = ""
	# 	# Secondary
	# 	if id_hacase.id == 2 :
	# 		monitoritemlist = MonitorItemList.objects.filter(id_dbtype__id=id_dbtype.id)
	# 	else :
	# 		monitoritemlist = MonitorItemList.objects.filter(id_dbtype__id=id_dbtype.id, id_hacase=id_hacase)		

	# 	for item in monitoritemlist :

	# 		new_obj = DBDetailMonitorItemList(
	# 			id_dbdetail= obj,
	# 			id_monitoritemlist= item,
	# 			compare_case= item.compare_case,
	# 			limit_value= item.limit_value,
	# 			risk_level= item.risk_level,
	# 			reg_dtm= datetime.datetime.now(),
	# 			id_reg_user= request.user,
	# 		)
	# 		new_obj.save()


admin.site.register(DbDetail, DbDetailAdmin)

class DBDetailMonitorItemListAdmin(admin.ModelAdmin):
	autocomplete_fields = [
	'id_dbdetail',
	'id_monitoritemlist',	
	]

	list_editable = [
						'limit_value',
	]

	search_fields = [ 'id_dbdetail__id','id_dbdetail__id_dblist__db_use']


	list_filter = ['id_dbdetail',]

	list_display = [
		'id_dbdetail',
		'id_monitoritemlist',
		'note1',
		'limit_value',
		'compare_case',
		'risk_level',
		'id_mod_user',
		'mod_dtm',

	]

	ordering = ['id_monitoritemlist__id_monitoritem__monitor_level','id_monitoritemlist__exp_order',]

	fields = [
		'id_dbdetail',
		'id_monitoritemlist',
		'compare_case',
		'limit_value',
		'risk_level',
	]

	list_per_page = 100

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(DBDetailMonitorItemList, DBDetailMonitorItemListAdmin)




class MetaReqListStack(admin.TabularInline):

    fk_name = 'id_metareq'
    # list_select_related = ('id_tablelist_code_table',)
    model = MetaReqList
    extra = 0
    autocomplete_fields =('id_tablelist','id_dblist',)
    readonly_fields = ('div',)
    # raw_id_fields = ('id_columnlist',)
    list_display = (
    	'div',
    	'id_tablelist',
    	'id_dblist',
    	'column_id',
    	'col_comments',
    	'pk_yn',
    	'not_null',
    	'column_name',
    	'data_type',
    	'change_list',
    	'change_reason',
    	'privacy_list',
    	'data_default',
    	           )

    fields = [
    		'div',
	    	'column_id',
	    	'col_comments',
	    	'pk_yn',
	    	'not_null',
	    	'column_name',
	    	'data_type',
	    	'privacy_list',
    		]
    ordering = ('column_id',)


class MetaReqAdmin(admin.ModelAdmin):

	inlines = (MetaReqListStack, )

	list_display_links = ['title',]
	list_editable = ['dba_dev_yn',
		'req_prod_yn',
		'pl_prod_yn',
		'dba_prod_yn',
		'check_prod_exec_yn',
		'dist_dtm',]

	autocomplete_fields = [
	'id_reg_user',
	'id_pl_dev',
	'id_pl_prod',
	'id_dba_dev',
	'id_dba_prod',
	'id_da_dev',
	'id_req_prod',
	'id_tablelist',
	]


	list_display = [
		'id',
		'id_dblist',		
		'title',
		'dba_dev_yn',
		'req_prod_yn',
		'pl_prod_yn',
		'dba_prod_yn',
		'check_prod_exec_yn',
		'id_dba_dev',
		'id_reg_user',
		'dist_dtm',
		'id_pl_prod',
	]

	ordering = ['-id']

	fields = [
		'id_dblist',
		'id_tablelist',
		'obj_new',
		'obj_class',
		'title',
		'table_name',
		'table_comments',
		'req_contents',
		'req_script',
		'id_reg_user',
		'id_dba_dev',
		'dba_dev_yn',
		'id_req_prod',
		'req_prod_yn',
		'dist_dtm',
		'id_pl_prod',
		'pl_prod_yn',
		'id_dba_prod',
		'dba_prod_yn',
		'check_prod_exec_yn',
	]

admin.site.register(MetaReq, MetaReqAdmin)


class SendEmailTargetListAdmin(admin.ModelAdmin):


	list_editable = [
		'send_case',
		'id_receive_user',
		]

	autocomplete_fields = [
	'id_receive_user',
	]


	list_display = [
	'id',
		'send_case',
		'id_receive_user',
		'reg_dtm',
	]

	ordering = ['-id']

	fields = [
		'send_case',
		'id_receive_user',

	]

admin.site.register(SendEmailTargetList, SendEmailTargetListAdmin)

class MetaReqWeekDayAdmin(admin.ModelAdmin):

	list_editable = ['check_prod_exec_yn','pl_prod_yn','pl_prod_dtm',]

	list_display_links = ['title',]

	list_display = [
	    'id',
		'check_prod_exec_yn',
		'dba_prod_yn',
		'id_dblist',
		'title',
		'id_dba_dev',
		'id_reg_user',
		'dist_dtm',
		'id_pl_prod',
		'pl_prod_yn',
		'pl_prod_dtm',
	]

	fields = [
		'id_dblist',
		'title',
	]

	def get_actions(self, request):
	    actions = super().get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	actions = ['update_chk','update_unchk','complete_prod']

	# check_prod_exec_yn = ( ('1','정기반영 대상'),('0','대상 아님'))
	# req_prod_yn = ( ('0','승인 전'), ('1','승인'),('2','반려'))

	def update_chk(self, request, queryset):
		queryset.update(check_prod_exec_yn='1')
	update_chk.short_description = """[지정] 선택된 대상 항목을 모두 "금주 정기 반영 대상"으로 지정합니다."""

	# def update_unchk(self, request, queryset):
	# 	queryset.update(check_prod_exec_yn='0')

	# update_unchk.short_description = """[해제] 선택된 대상 항목을 모두 "금주 정기 반영 대상" 해제합니다."""

	def complete_prod(self, request, queryset):
		queryset.update(dba_prod_dtm=datetime.datetime.now(),
			            dba_prod_comment='운영 반영 완료되었습니다.',
			            dba_prod_yn='1',
			            id_dba_prod=request.user)

	complete_prod.short_description = """[완료] 선택된 대상 항목을 모두 운영 반영 완료로 변경합니다."""


	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(dist_dtm__isnull=False,
			             dist_dtm__lt=datetime.datetime.now() + datetime.timedelta(days=1),
			             dist_dtm__gt=datetime.datetime.now() - datetime.timedelta(hours=9),
			             pl_prod_yn='1',
			             dba_prod_yn__in=['0','1','2']
			            )

admin.site.register(MetaReqWeekDay, MetaReqWeekDayAdmin)


# class MonitorManageAdmin(admin.ModelAdmin):

# 	list_editable = ['monitor_yn','alert_yn','use_yn',]

# 	list_filter = [
# 		'use_yn',
# 		'monitor_yn',
# 		'alert_yn',	
# 		'oper_cd',
# 	    'db_order',	    
# 	    'id_hacase',	    
# 		'id_dblist__db_use',	
# 	]

	

# 	list_display = [
# 	    'id',
# 	    'oper_cd',
# 	    'db_order',
# 	    'get_db_use',
# 	    'id_hacase',	    
# 	    'svr_ip',
# 	    'get_dbms_type',
# 	    'use_yn',
# 		'monitor_yn',
# 		'alert_yn',	
# 	]	

# 	def get_db_use(self, obj):
# 		return obj.id_dblist.db_use
# 	get_db_use.short_description = 'DB명'

# 	def get_dbms_type(self, obj):
# 		return obj.id_dblist.id_dbtype
# 	get_dbms_type.short_description = 'DBMS'

# 	ordering = ('id_dblist__db_use','db_order')
# 	list_per_page = 1000


# admin.site.register(MonitorManage, MonitorManageAdmin)


class MonitorManagementAdmin(admin.ModelAdmin):	

	filter_horizontal = ('id_dbdetail',)
	list_display_links = ('monitor_name',)
	list_editable = (
		'alert_yn',
		# 'monitor_yn',
		)


	list_display = [
		'monitor_name',
		'alert_yn',
		# 'monitor_yn',
		'id_mod_user',
		'mod_dtm',
	]

	fields = [	'monitor_name',
				'id_dbdetail',
				# 'monitor_yn',
				'alert_yn',]

	def save_model(self, request, obj, form, change):
		obj.id_mod_user = request.user
		obj.save()

	# 삭제 방지
	def has_delete_permission(self, request, obj=None):
		return False

	ordering = ['id',]



admin.site.register(MonitorManagement, MonitorManagementAdmin)







class MonitorTablespaceAdmin(admin.ModelAdmin):

	list_editable = ['limit_value','explain',]

	list_display_links = ['tablespace_name',]


	list_display = [
		'get_oper_cd',
		'id_dbdetail',
		'tablespace_name',
		'limit_value',
		'explain',
		'reg_dtm',
		'mod_dtm',
		'id_mod_user',
	]

	fields = [
		'id_dbdetail',
		'tablespace_name',
		'limit_value',
		'explain',
		'reg_dtm',
		'mod_dtm',

	]


	search_fields = ['tablespace_name','id_dbdetail__id_dblist__db_use','id_dbdetail__id',]
	list_filter = ['id_dbdetail',]

	def save_model(self, request, obj, form, change):
		obj.id_mod_user = request.user
		obj.save()

	def get_oper_cd(self, obj):
		return obj.id_dbdetail.oper_cd.oper_cd
	get_oper_cd.short_description = '운영구분'

admin.site.register(MonitorTablespace, MonitorTablespaceAdmin)


class DomainAndDbListAdmin(ImportExportMixin, admin.ModelAdmin):

	autocomplete_fields =('it_manager','dev_manager','id_domain','id_dblist',)
	list_editable = ('erd_user',)
	list_display_links = ['id_domain',]
	search_fields = ['id_dblist__db_use','id_domain__domain_name',]

	list_display = (		
		'id_dblist',
		'id_domain',
		'get_id_domain',
		'get_it_manager',
		'get_dev_manager',
		'erd_user',
		'id_reg_user',
		'id_mod_user',
		)
	fields = (
		'id_dblist',
		'id_domain',
		'erd_user',
		'it_manager',
		'dev_manager'
		)
	search_fields = (
		# 'it_manager__first_name',
		# 'dev_manager__first_name',
		'id_dblist__db_use',
		'id_domain__domain_name'
		)
	ordering = (
		'id_dblist',
		'id_domain',
		)
	list_filter = (
		'id_domain',
		'id_dblist',
		)
	list_per_page = 30

	ordering = ['id_dblist__exp_order','id_domain__domain_name']

	def get_id_domain(self, obj):
		return obj.id_domain.id
	get_id_domain.short_description = '도메인ID'

	def get_sql_text(self, obj):
		# return ", ".join([p.first_name for p in obj.it_manager.all()])
		return obj.sql_text[0:100]
	get_sql_text.short_description = '관련SQL(100글자만)'



	def get_it_manager(self, obj):
		return ", ".join([p.first_name for p in obj.it_manager.all()])
	get_it_manager.short_description = 'GSSHOP 담당자'


	def get_dev_manager(self, obj):
		return ", ".join([p.first_name for p in obj.dev_manager.all()])
	get_dev_manager.short_description = '개발 담당자'

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(DomainAndDbList, DomainAndDbListAdmin)

class MenuPermissionAdmin(admin.ModelAdmin):

	autocomplete_fields =(
		'id_menulist',
		'id_grantee_user',
		)

	list_display = (
		'id_grantee_user',
		'id_menulist',
		'id_reg_user',
		'id_mod_user',
		'reg_dtm',
		'mod_dtm',
		)
	fields = (
		'id_grantee_user',
		'id_menulist',
		)
	search_fields = (
		'id_grantee_user__first_name',
		)
	ordering = (
		'id_grantee_user',
		)
	list_filter = (
		'id_menulist',
		)
	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(MenuPermission, MenuPermissionAdmin)


# class ColumnListAdmin(SummernoteModelAdmin):
# 	# autocomplete_fields =('id_columnlist',)
# 	list_display_links = ['column_name',]
# 	fields = [
# 			'db_use',
# 			'owner',
# 			'table_name',
# 			'comments',
# 			'column_name',
# 			'col_comments',
# 			'code_key',
# 			'column_explain',
# 		]
# 	search_fields = ['table_name']
# 	list_display = ['owner','table_name','comments','column_id','column_name','col_comments','column_explain']
# 	# list_filter = ['id_tablelist__id_dblist__db_use']
# 	list_filter = ['db_use']
# 	# list_editable = (
# 	# 	'column_explain',
# 	# 	)
# 	ordering = ('owner','table_name','column_id')

# 	def get_exp_order(self, obj):
# 	        return obj.id_tablelist.exp_order

# 	# def get_queryset(self, request):
# 	# 	qs = super().get_queryset(request)
# 	# 	return qs.filter(id_tablelist__exp_order__lt = 5, owner = 'DHUB_OWN')


# # admin.site.register(ColumnList)
# admin.site.register(ColumnList, ColumnListAdmin)


# TabularInline
# class ColumnListStack(admin.StackedInline):
class ColumnListStack(admin.TabularInline):

    fk_name = 'id_tablelist'
    # list_select_related = ('id_tablelist_code_table',)
    model = ColumnList
    # extra = 1
    autocomplete_fields =('id_tablelist_code_table',)
    # raw_id_fields = ('id_columnlist',)
    list_display = ('column_name',
    	            'col_comments')


    search_fields = []

    readonly_fields = [
		    'column_id',
    		'column_name',
    		'col_comments',
    		'pk_yn',
    		'data_type',
    		]

    fields = [
    		'column_id',
    		'column_name',
    		'col_comments',
    		'pk_yn',
    		'data_type',
    		'secu_yn',
    		]
    ordering = ('column_id',)

    def get_queryset(self, request):
    	qs = super().get_queryset(request)
    	return qs.filter(drop_yn="0")



	# def short_comments(self, TableList):
	# 	return TableList.comments[:10]

class TableListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''

	list_editable = ['id_domain',]
	inlines = (ColumnListStack, )
	autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_tablelist_member_table',)
	# autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_domainlist')
	# raw_id_fields = ('id_domainlist',)

	list_display_links = ['table_name']
	list_display = [
		'id_dblist',
		'oper_cd',
		'owner',
		'table_name',
		'comments',
		'tablespace_name',
		'id_domain',
		# 'id_user_it_manager',
		# 'id_user_dev_manager',
		'id_reg_user',
		'reg_dtm',
		]
	readonly_fields = [
		'id_dblist',
		# 'id_domainlist',
		'owner',
		'table_name',
		'comments',
		]
	fields = [
		'id_dblist',
		# 'id_domainlist',
		'owner',
		'table_name',
		'comments',
		'secu_yn',
		'cdc_yn',
		]
	# list_editable = (
	# 	'channel_type',
	# 	'domain_name',
	# 	)
	search_fields = (
		'table_name',
		'comments',
		)
	ordering = (
		'id_dblist',
		'owner',
		'table_name',
		)
	list_filter = (
		'id_dblist',
		)

	list_per_page = 30




	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()


	# def short_comments(self, TableList):
	# 	return TableList.comments[:10]

# admin.site.register(ColumnList, SummernoteModelAdmin)
admin.site.register(TableList, TableListAdmin)

# class DataSearchAdmin(admin.ModelAdmin):
# 	'''
# 	Admin View for Bbs
# 	'''

# 	inlines = (ColumnListStack, )
# 	autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_tablelist_member_table',)
# 	# autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_domainlist')
# 	# raw_id_fields = ('id_domainlist',)

# 	list_display_links = ['table_name']
# 	list_display = [
# 		'id_dblist',
# 		'id_domainlist',
# 		'owner',
# 		'table_name',
# 		'comments',
# 		'tablespace_name',
# 		'id_user_it_manager',
# 		'id_user_dev_manager',
# 		'id_reg_user',
# 		'reg_dtm',
# 		'id_mod_user',
# 		'mod_dtm',
# 		'exp_order',
# 		]
# 	fields = [
# 		'id_dblist',
# 		'id_domainlist',
# 		'owner',
# 		'table_name',
# 		'pk_column',
# 		'sql_exp_column',
# 		'comments',
# 		'id_tablelist_parent_table',
# 		# 'data_search_psbl_yn',
# 		'id_tablelist_member_table',
# 		'config_sql',
# 		'exp_order',
# 		]
# 	# list_editable = (
# 	# 	'channel_type',
# 	# 	'domain_name',
# 	# 	)
# 	search_fields = (
# 		'table_name',
# 		'comments',
# 		)
# 	ordering = (
# 		'id_dblist',
# 		'owner',
# 		'table_name',
# 		)
# 	list_filter = (
# 		'id_dblist',
# 		)

# 	list_per_page = 10

# 	def save_model(self, request, obj, form, change):
# 		if change :
# 			obj.id_mod_user = request.user
# 		else :
# 			obj.id_reg_user = request.user
# 		obj.save()

# 	# def short_comments(self, TableList):
# 	# 	return TableList.comments[:10]

# 	def get_queryset(self, request):
# 		# qs = super().get_queryset(request)
# 		# qs = super(DataSearchAdmin, self).get_queryset(request)
# 		# return super().get_queryset(request).filter(exp_order > 0)
# 		return DataSearch.objects.filter(exp_order > 0)

# admin.site.register(DataSearch, DataSearchAdmin)




class ProcessListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
		'id',
		'ordering',
		'process_nm',
		'reg_dtm',
		'mod_dtm',
		'id_reg_user',
		'id_mod_user'
		)
	fields = [
		'ordering',
		'process_nm',
		]
	search_fields = (
		'ordering',
		'process_nm',
		)
	list_editable = (
		'ordering',
		'process_nm',
		)
	# ordering = (
	# 	'oper_cd',
	# 	'db_nm',
	# 	)
	# list_filter = (
	# 	'oper_cd',
	# 	)
	list_per_page = 30

	# def get_queryset(self, request):
	# 	qs = super().get_queryset(request)
	# 	return qs.filter(oper_cd="운영")
	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()


admin.site.register(ProcessList, ProcessListAdmin)

class DataListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	# autocomplete_fields =('id_domainlist','id_reg_user','id_mod_user','id_dblist','id_tablelist',)
	# autocomplete_fields =('id_processlist','id_tablelist_member_table',)
	autocomplete_fields =('id_req_users','id_mod_psbl_users',)

	list_display_links = ['data_title']
	list_display = [
			'id',
			'data_title',
			'id_dblist',
			'id_domain',
			'realoretl',
			'privacy_yn',
			'prov_yn1',
			'prov_yn2',
			'exp_yn',
			'id_prov_user1',
			'id_prov_user2',
			'id_reg_user',
			'id_mod_user',
			'reg_dtm',
			'mod_dtm',

			# 'data_search_psbl_yn',
			# 'exp_order',
		]
	list_editable = [
				'prov_yn1',
				'prov_yn2',
				'id_domain',
			]
	fields = [
			'id_dblist',
			'id_domain',
			'data_title',
			'data_explain',
			'sql_text',
			'privacy_yn',
			'realoretl',
			'id_req_users',
			'id_mod_psbl_users',
			'prov_yn1',
			'prov_yn2',
			'exp_yn',
			'exp_order',
		]
	ordering = (
		'-reg_dtm',
		)
	list_filter = (
		'data_title',
		)

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user

			if obj.privacy_yn == 0 :
				obj.prov_yn1 = 1

		obj.save()

admin.site.register(DataList, DataListAdmin)


class DataRequestAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	# autocomplete_fields =('id_domainlist','id_reg_user','id_mod_user','id_dblist','id_tablelist',)
	autocomplete_fields =('id_prov_user',)


	list_display_links = ['data_title']
	list_display = [
			'id',
			'id_reg_user',
			'id_mod_user',
			'id_datalist',
			'data_title',
			'data_explain',
			'prov_yn',
			'poss_view_dtm',
			'reg_dtm',
			'mod_dtm',
			'prov_yn_dtm',
			'id_prov_user',
		]
	fields = [
			'id_datalist',
			'data_title',
			'data_explain',
			'prov_yn',
			'id_prov_user',
			'poss_view_dtm',
		]
	ordering = (
		'-reg_dtm',
		)

	list_editable = (
		'poss_view_dtm',
		)

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(DataRequest, DataRequestAdmin)

class BatchListAdmin(admin.ModelAdmin):

	list_display = [
			'batch_title',
			'batch_system_name',
			'target_table',
			'id_dbtype',
			'batch_type',
			'batch_order',
			'truncate_yn',
			'use_yn',
			'id_reg_user',
			'id_mod_user',
			'reg_dtm',
			'mod_dtm',
		]
	fields = [
			'batch_title',
			'batch_system_name',
			'batch_type',
			'target_table',
			'id_dbtype',
			'sql_text',
		]
	list_editable = (
		'truncate_yn','use_yn','batch_order',
		)
	search_fields = (
		'batch_title',
		)
	ordering = (
		'batch_type','batch_order'
		)

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()



admin.site.register(BatchList, BatchListAdmin)



class TuningStatusAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
		'id',
		'status',
		'reg_dtm',
		'mod_dtm',
		'id_reg_user',
		'id_mod_user',
		)
	fields = [
		'status',
		]
	list_editable = (
		'status',
		)
	ordering = (
		'mod_dtm',
		)

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(TuningStatus, TuningStatusAdmin)

class ProjectListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
			'title',
			'start_dtm',
		)
	fields = [
		'title',
		'start_dtm',
		]

	ordering = (
		'start_dtm',
		)

	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

admin.site.register(ProjectList, ProjectListAdmin)


class UserExecuteSQLAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
		'get_sql_text',
		'id_dbdetail',
		'id_reg_user',
		'reg_dtm',
		'execute_time',
		)
	fields = [
		'sql_text',
		'id_reg_user',
		'execute_time',
		]
	ordering = ['-reg_dtm']

	search_fields = ['id_reg_user']

	readonly_fields = [
	'sql_text',
	'id_reg_user',
	'reg_dtm',
	'execute_time',
	]

	def get_sql_text(self, obj):
		# return ", ".join([p.first_name for p in obj.it_manager.all()])
		return obj.sql_text[0:100]
	get_sql_text.short_description = '관련SQL(100글자만)'

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(UserExecuteSQL, UserExecuteSQLAdmin)



class TuningListAdmin(SummernoteModelAdmin):
	'''
	Admin View for Bbs
	'''
	autocomplete_fields =('id_reg_user','id_tuning_user',)

	list_display = (
		'id',
		'title',
		'sql_type',
		'id_domain',
		'id_dblist',
		'id_tuningstatus',
		'asis_elapsed_time',
		'tobe_elapsed_time',
		'id_reg_user',
		'id_tuning_user',
		'tuning_dtm',
		'dist_dtm',
		)
	fields = [
		'title',
		'sql_type',
		'id_domain',
		'id_dblist',
		'id_tuningstatus',
		'asis_elapsed_time',
		'tobe_elapsed_time',
		'id_reg_user',
		'id_tuning_user',
		'tuning_dtm',
		'dist_dtm',
		]
	ordering = (
		'-reg_dtm',
		)

	list_per_page = 30

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(TuningList, TuningListAdmin)




class MenuListAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
		'id',
		'use_yn',
		'menu_name',
		'url',
		'default_permission_yn',
		'menu_explain',
		'reg_dtm',
		'mod_dtm',
		)
	fields = [
		'menu_name',
		'menu_explain',
		'default_permission_yn',
		]
	ordering = (
		'-use_yn',
		)
	list_editable = (
		'use_yn',
		'url',
		'menu_name',
		'default_permission_yn',
		)
	search_fields = (
		'menu_name',
		)

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(MenuList, MenuListAdmin)


class UserVisitAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''
	list_display = (
		'name',
		'sabun',
		'team_name',
		'id_menulist',
		'reg_dtm',
		)
	fields = [
		'name',
		'sabun',
		'team_name',
		'id_menulist',
		'reg_dtm',
		]
	search_fields = (
		'name',
		)
	list_filter = (
		'reg_dtm',
		'name',
		'team_name',
		'id_menulist',
		)
	ordering = (
		'-reg_dtm',
		)

admin.site.register(UserVisit, UserVisitAdmin)



# class RegisterDataAdmin(admin.ModelAdmin):

# 	autocomplete_fields =('id_req_users','id_mod_psbl_users')

# 	list_display_links = ['data_title',]

# 	list_display = [
# 		'id_dblist',
# 		'data_title',
# 		'data_explain',
# 		'privacy_yn',
# 		'realoretl',
# 		'id_prov_user1',
# 		'id_prov_user2',
# 		'id_mod_user',
# 		'mod_dtm',
# 		]
# 	fields = [
# 		'id_dblist',
# 		'data_title',
# 		'id_req_users',
# 		'id_mod_psbl_users',
# 		'privacy_yn',
# 		'realoretl',
# 		'data_explain',
# 		'sql_text',
# 		]


# 	list_per_page = 30

# 	def get_queryset(self, request):
# 		qs = super().get_queryset(request)
# 		return qs.filter(Q(id_mod_psbl_users = request.user) and Q(id_mod_user = request.user))

# 	def save_model(self, request, obj, form, change):
# 		if change :
# 			obj.id_mod_user = request.user
# 		else :
# 			obj.id_reg_user = request.user
# 			obj.id_mod_user = request.user
# 		obj.exp_yn = 1
# 		obj.save()

# admin.site.register(RegisterData, RegisterDataAdmin)

class SecureApproveAdmin(admin.ModelAdmin):

	# autocomplete_fields =('id_mod_user','id_req_user',)


	list_display = [
		'data_title',
		'data_explain',
		'prov_yn1_text',
		'privacy_yn',
		'prov_yn1',
		'id_prov_user1',
		'prov_yn1_dtm',
		'id_reg_user',
		'mod_dtm',
		]
	fields = [
		'data_title',
		'data_explain',
		'id_reg_user',
		'id_req_users',
		'privacy_yn',
		'prov_yn1',
		'prov_yn1_text',
		'sql_text',
		]
	search_fields = (
		'data_title',
		)
	ordering = (
		'prov_yn1',
		'-mod_dtm',
		)
	readonly_fields = [
	'data_title',
	'data_explain',
	'id_reg_user',
	'id_req_users',
	'sql_text',
	]


	list_per_page = 30

	def clean(self):
		if self.prov_yn1_text == ""  :
			raise ValidationError("Zone name is not given!")

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(Q(privacy_yn = 1))

	def save_model(self, request, obj, form, change):
		print(change)
		if change :
			if obj.prov_yn1 == "0" :
				obj.id_prov_user1 = None
				obj.prov_yn1_dtm = None
			else :
				obj.id_prov_user1 = request.user
				obj.prov_yn1_dtm = datetime.datetime.now()
		obj.save()

admin.site.register(SecureApprove, SecureApproveAdmin)

class DataDocumentPRDAdmin(admin.ModelAdmin):
	'''
	Admin View for Bbs
	'''

	# inlines = (ColumnListStack, )
	# autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_tablelist_member_table',)
	# autocomplete_fields =('id_dblist','id_tablelist_parent_table','id_domainlist')
	# raw_id_fields = ('id_domainlist',)

	# autocomplete_fields =('id_columnlist',)
	list_display_links = ['column_name',]
	fields = [
			'db_use',
			'owner',
			'table_name',
			'comments',
			'column_name',
			'col_comments',
			'column_explain',
		]
	search_fields = ['table_name']
	list_display = ['owner','table_name','comments','column_id','column_name','col_comments','column_explain']
	# list_filter = ['id_tablelist__id_dblist__db_use']
	list_filter = ['db_use']
	# list_editable = (
	# 	'column_explain',
	# 	)
	ordering = ('owner','table_name','column_id')

	def get_exp_order(self, obj):
	        return obj.id_tablelist.exp_order



	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(Q(exp_order__lt = 20, owner = 'SMTC_OWN'))


	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

admin.site.register(DataDocumentPRD, DataDocumentPRDAdmin)

class UserListAdmin(admin.ModelAdmin):


	list_editable = ['request_status',]

	list_display = [
		'id_dblist',
		'request_status',
		'oper_cd',
		'username',
		'id_user_name',
		'status',
		'created',
		'profile',
		'reg_dtm',
		'mod_dtm',
	]

	fields = [
		'id_dblist',
		'oper_cd',
		'username',
		'id_user_name',
		'status',
		'profile',
		# 'reg_dtm',
		# 'mod_dtm',
		'request_status',
	]

	readonly_fields = [
		'id_user_name',
	]

	list_filter = ['oper_cd',]

	ordering = ['id_dblist','username',]

	search_fields = ['id_user_name__first_name']

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(Q(request_status = 0))


admin.site.register(UserList, UserListAdmin)

class UserRequestAccountOpenHistAdmin(admin.ModelAdmin):


	list_display = [
		'id_userlist',
		'get_db_use',
		'id_reg_user',
		'reg_dtm',
		'id_approver',
		'approv_dtm',
	]

	fields = [
		'id_userlist',
		'id_approver',
		'approv_dtm',
		'id_reg_user',
	]

	readonly_fields = [
		'id_userlist',
		'id_approver',
		'approv_dtm',
		'id_reg_user',
	]



	search_fields = ['id_reg_user__first_name']

	# def save_model(self, request, obj, form, change):
	# 	obj.id_reg_user = request.user
	# 	obj.save()

	def get_db_use(self, obj):
		return obj.id_userlist.id_dblist.db_use
	get_db_use.short_description = 'DB명'

	def delete_model(self, request, obj):
		print(obj.id_userlist)
		userlist = UserList.objects.get(id=obj.id_userlist.id)
		userlist.request_status = '0'
		userlist.save()

	def get_actions(self, request):
	    actions = super().get_actions(request)
	    if 'delete_selected' in actions:
	        del actions['delete_selected']
	    return actions

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(Q(approv_dtm = None))







admin.site.register(UserRequestAccountOpenHist, UserRequestAccountOpenHistAdmin)

class UserRequestTabPrivHistAdmin(admin.ModelAdmin):

	list_editable = ['approv_yn',]

	list_display = [
		'id_userlist',
		'approv_yn',
		'priv',
		'id_objectlist',
		'id_reg_user',
		'reg_dtm',
		'id_approver',
		'approv_dtm',
		'object_type',
		'req_reason',
	]

	fields = [
		'id_userlist',
		'id_objectlist',
		'id_approver',
		'approv_dtm',
		'id_reg_user',
		'priv',
		'object_type',
		'req_reason',
		'approv_yn',
	]

	readonly_fields = [
		'id_userlist',
		'id_objectlist',
		'id_reg_user',
		'id_approver',
	]

	search_fields = ['id_reg_user__first_name']

	ordering = ['-reg_dtm',]

	# def get_queryset(self, request):
	# 	qs = super().get_queryset(request)
	# 	return qs.filter(Q(approv_yn = 0))



admin.site.register(UserRequestTabPrivHist, UserRequestTabPrivHistAdmin)

class MetaGrantListAdmin(admin.ModelAdmin):

	autocomplete_fields =('id_dblist',)
	list_display = [
		'id_dblist',
		'app_service',
	]
	fields = [
		'id_dblist',
		'app_service',
	]
	list_per_page = 100


admin.site.register(MetaGrantList, MetaGrantListAdmin)

class MetaGrantDetailAdmin(admin.ModelAdmin):

	list_display = [
		'get_db_use',
		'id_metagrantlist',
		'role',
		'crud',
	]
	fields = [
		'id_metagrantlist',
		'role',
		'crud',
	]

	ordering = [
		'id_metagrantlist',
	]

	search_fields = ['id_metagrantlist__id_dblist__db_use',]

	def get_db_use(self, obj):
		# return ", ".join([p.first_name for p in obj.it_manager.all()])
		return obj.id_metagrantlist.id_dblist
	get_db_use.short_description = 'DB명'

	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()


admin.site.register(MetaGrantDetail, MetaGrantDetailAdmin)


class MonitorItemAdmin(admin.ModelAdmin):

	
	
	list_display_links = ['item_nm',]
	list_editable = ['sms_message','exp_order']

	list_display = [field.name for field in MonitorItem._meta.fields ]
	fields = [field.name for field in MonitorItem._meta.fields if field.name not in ["id","id_reg_user",'mod_dtm',] ]


	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

	ordering = ['exp_order',]

admin.site.register(MonitorItem, MonitorItemAdmin)


class MonitorItemListAdmin(admin.ModelAdmin):

	list_editable = ['use_yn','risk_level','limit_value','compare_case','graph_yn','id_hacase','id_dbtype']
	list_display_links = ['id_monitoritem',]
	fields = [
			'id_monitoritem',
			'id_hacase',
			'graph_yn',
			'use_yn',
			'relative_case',
			'limit_value',			
			'compare_case',
			'risk_level',
			'id_dbtype',
			'sql_text',
			'column_name',
			'linux_cmd',
			'unix_cmd',
		]
	list_display = [	
					'id',				
					'id_monitoritem',
					'column_name',
					'id_dbtype',
					'id_hacase',
					'graph_yn',					
					'limit_value',					
					'compare_case',
					'risk_level',
					'use_yn',					
					'id_reg_user',
					'reg_dtm',

				]
	ordering = ('id_dbtype','id_monitoritem',)

	search_fields = ['id_monitoritem__item_nm',]



	def save_model(self, request, obj, form, change):
		obj.id_reg_user = request.user
		obj.save()

admin.site.register(MonitorItemList, MonitorItemListAdmin)


class MonitorItemLogAdmin(admin.ModelAdmin):

	
	list_display = [					
					'get_id_dbdetail',
					'get_id_monitoritemlist',
					'get_note1',					
					'monitor_value',
					'error_yn',
					'elapsed_time',
					'error_msg',
					'reg_dtm',
				]
	ordering = ('-reg_dtm',)
	list_filter = ['error_yn','id_dbdetailmonitoritemlist__id_monitoritemlist','id_dbdetailmonitoritemlist__id_dbdetail',]

	search_fields = ['id_dblist__db_use',]

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(reg_dtm__gt=datetime.datetime.now() - datetime.timedelta(days=1),)

	def get_id_dbdetail(self, obj):
		return obj.id_dbdetailmonitoritemlist.id_dbdetail
	get_id_dbdetail.short_description = 'DB'

	def get_id_monitoritemlist(self, obj):
		return obj.id_dbdetailmonitoritemlist.id_monitoritemlist
	get_id_monitoritemlist.short_description = '모니터링대상1'

	def get_note1(self, obj):
		return obj.id_dbdetailmonitoritemlist.note1
	get_note1.short_description = '모니터링대상2'


admin.site.register(MonitorItemLog, MonitorItemLogAdmin)


class OsUserAdmin(admin.ModelAdmin):

	autocomplete_fields = ['id_dbdetail',]

	fields = [					
					'id_dbdetail',
					'user_name',
					'password',
					'use_yn',				
				]

	list_display = [					
					'id_dbdetail',
					'user_name',
					'password',
					'use_yn',
					'mod_dtm',
					'id_mod_user',
				]

	search_fields = ['id_dbdetail__id_dblist__db_use',]

	ordering = ['id_dbdetail__id_dblist__exp_order','id_dbdetail__oper_cd','id_dbdetail__db_order']

	search_fields = ['id_dbdetail__id_dblist__db_use',]

	def save_model(self, request, obj, form, change):
		obj.id_mod_user = request.user
		obj.save()


admin.site.register(OsUser, OsUserAdmin)

class DbUserAdmin(admin.ModelAdmin):

	autocomplete_fields = ['id_dblist','id_req_user',]

	fields = [					
					'id_dblist',
					'oper_cd',
					'username',
					'password',
					'conn_ip',
					'id_req_user',
					'req_reason',					
				]

	list_display = [					
					'id_dblist',
					'oper_cd',
					'username',
					'password',
					'conn_ip',
					'req_reason',
					'id_req_user',
					'id_mod_user',
					'mod_dtm',
					'drop_yn',
					'get_ddl',
				]

	search_fields = ['id_dblist__db_use','username','id_req_user__first_name']

	ordering = ['-mod_dtm','id_dblist__exp_order','username']

	list_filter = ['drop_yn', 'oper_cd','id_dblist__db_use']

	list_per_page = 5

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs

	def save_model(self, request, obj, form, change):
		if change :
			obj.id_mod_user = request.user
		else :
			obj.id_reg_user = request.user
			obj.id_mod_user = request.user
		obj.save()

	def get_ddl(self, obj):
			DDL = ""
			
			if obj.password is None :
				return ""

			if obj.id_dblist.id_dbtype.id_db.db_type == "ORACLE" :
				DDL = 'CREATE USER {username} IDENTIFIED BY "{password}" profile gs_app;' + '<br>' + \
				      'GRANT CREATE SESSION TO {username};' + '<br>' + \
				      '-- GRANT SELECT,UPDATE,DELETE,INSERT ON [owner].[table_name] TO {username};'  + '<br>' + \
				      '-- GRANT SELECT ON [owner].[table_name] TO {username};'				      
			elif obj.id_dblist.id_dbtype.id_db.db_type in ["MYSQL","MARIADB"] :
				DDL = 'CREATE USER {username}@\'{ip}\' IDENTIFIED BY \'{password}\';' + '<br>' + \
				      'GRANT SELECT,UPDATE,DELETE,INSERT ON [db_nm].* TO {username}@\'{ip}\';'
			
			return format_html(DDL.format(username=obj.username,password=obj.password,ip=obj.conn_ip))
	get_ddl.short_description = '계정생성DDL'
	get_ddl.allow_tags = True


admin.site.register(DbUser, DbUserAdmin)


admin.site.register(AirflowDagManage)


