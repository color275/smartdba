from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from database import views

from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = "SmartDBA"
admin.site.site_title = "SmartDBA"
admin.site.index_title = "Welcome to SmartDBA"



urlpatterns = [

    path('', views.main, name='main'),
    path('page404/', views.page404, name='page404'),

    ###########################################################################
    ## Dashboard
    ###########################################################################
    # path('dashboard/', views.dashboard, name='dashboard'),

    ###########################################################################
    ## 데이터 찾기
    ###########################################################################
    # path('dataSearchKeyword/', views.dataSearchKeyword, name='dataSearchKeyword'),
    # path('dataSearchKeyword/<str:keyword>', views.dataSearchKeyword, name='dataSearchKeyword'),
    # path('dataSearchKeyword/<str:keyword>/<int:domain_id>', views.dataSearchKeyword, name='dataSearchKeyword'),
    path('dataView/', views.dataView, name='dataView'),

    # path('dataSearchDomain/<int:domain_id>', views.dataSearchDomain, name='dataSearchDomain'),
    # path('dataSearchFlow/<int:column_id>/<int:domain_id>', views.dataSearchFlow, name='dataSearchFlow'),

    ###########################################################################
    ## SQL 실행
    ###########################################################################
    path('executeSQL/', views.executeSQL, name='executeSQL'),
    path('executeSQLLV/', views.executeSQLLV.as_view(), name='executeSQLLV'),

    ########################l##################################################
    ## 개발
    ###########################################################################
    path('databaseMap/', views.databaseMap, name='databaseMap'),
    path('databaseList/', views.databaseList, name='databaseList'),
    path('msaTable/', views.msaTable, name='msaTable'),
    path('msaTableTest/', views.msaTableTest, name='msaTableTest'),
    # path('MetaRegLV/', views.MetaRegLV.as_view(), name='MetaRegLV'),
    path('MetaReqLV/', views.MetaReqLV.as_view(), name='MetaReqLV'),
    path('CreateDDLLV/', views.CreateDDLLV.as_view(), name='CreateDDLLV'),

    path('MetaScriptDownload/', views.MetaScriptDownload, name='MetaScriptDownload'),
    path('TotalScriptDownload/', views.TotalScriptDownload, name='TotalScriptDownload'),

    path('MetaReqListLV/<int:id_metareq>', views.MetaReqListLV.as_view(), name='MetaReqListLV'),
    path('MetaReqListUV/<int:id_metareq>', views.MetaReqListUV.as_view(), name='MetaReqListUV'),
    path('MetaReqListCV/', views.MetaReqListCV.as_view(), name='MetaReqListCV'),
    path('howDatabaseConn/', views.howDatabaseConn, name='howDatabaseConn'),
    # path('tableSearch/', views.tableSearch, name='tableSearch'),

    path('UserListLV/', views.UserListLV.as_view(), name='UserListLV'),

    path('TuningListLV/', views.TuningListLV.as_view(), name='TuningListLV'),
    path('TuningListDV/<int:id>', views.TuningListDV.as_view(), name='TuningListDV'),
    path('TuningListCV/', views.TuningListCV.as_view(), name='TuningListCV'),
    path('TuningListUV/<int:id>', views.TuningListUV.as_view(), name='TuningListUV'),
    path('TuningListDeleteView/<int:pk>', views.TuningListDeleteView.as_view(), name='TuningListDeleteView'),

    path('DataListDelView', views.DataListDelView, name='DataListDelView'),

    path('DataListCreateView/', views.DataListCreateView.as_view(), name='DataListCreateView'),
    path('DataListUpdateView/<int:id>', views.DataListUpdateView.as_view(), name='DataListUpdateView'),
    path('DataListSelectView_Approve', views.DataListSelectView_Approve, name='DataListSelectView_Approve'),
    path('DataListUpdateView_Approve/<int:id>', views.DataListUpdateView_Approve.as_view(), name='DataListUpdateView_Approve'),

    path('DataRequestLV/', views.DataRequestLV.as_view(), name='DataRequestLV'),
    path('DataRequestCV/', views.DataRequestCV.as_view(), name='DataRequestCV'),
    path('DataRequestUV/<int:id>', views.DataRequestUV.as_view(), name='DataRequestUV'),

    path('DataSearchLV/', views.DataSearchLV.as_view(), name='DataSearchLV'),
    path('DataSearchLV/<str:keyword>', views.DataSearchLV.as_view(), name='DataSearchLV'),
    path('DataSearchDV/<int:id>', views.DataSearchDV.as_view(), name='DataSearchDV'),


    path('ObjectListLV/', views.ObjectListLV.as_view(), name='ObjectListLV'),
    path('ObjectListDV/<int:id>', views.ObjectListDV.as_view(), name='ObjectListDV'),

    path('TableListLV/', views.TableListLV.as_view(), name='TableListLV'),    

    path('GrantListLV/', views.GrantListLV.as_view(), name='GrantListLV'),

    path('StdWordLV/', views.StdWordLV.as_view(), name='StdWordLV'),
    path('StdDomainLV/', views.StdDomainLV.as_view(), name='StdDomainLV'),
    path('StdDivAttrLV/', views.StdDivAttrLV.as_view(), name='StdDivAttrLV'),
    

    path('ModelSMTCPrd/', views.ModelSMTCPrd.as_view(), name='ModelSMTCPrd'),
    path('ModelLV/', views.ModelLV.as_view(), name='ModelLV'),




    path('DBAWorkLV/', views.DBAWorkLV.as_view(), name='DBAWorkLV'),
    path('QuickLinkLV/', views.QuickLinkLV.as_view(), name='QuickLinkLV'),
    path('DBABatchLV/', views.DBABatchLV.as_view(), name='DBABatchLV'),
    path('MetaDV/<int:id>', views.MetaDV.as_view(), name='MetaDV'),
    path('OneDBMonitorLV/<int:id>', views.OneDBMonitorLV.as_view(), name='OneDBMonitorLV'),

    path('Autocomplete_User_Search/', views.Autocomplete_User_Search.as_view(), name='Autocomplete_User_Search'),
    path('Autocomplete_Domain/', views.Autocomplete_Domain.as_view(), name='Autocomplete_Domain'),
    path('Autocomplete_DbList/', views.Autocomplete_DbList.as_view(), name='Autocomplete_DbList'),
    path('Autocomplete_ExecuteSQL_DbList/', views.Autocomplete_ExecuteSQL_DbList.as_view(), name='Autocomplete_ExecuteSQL_DbList'),
    path('Autocomplete_DbList_Part/', views.Autocomplete_DbList_Part.as_view(), name='Autocomplete_DbList_Part'),
    path('Autocomplete_OperCd/', views.Autocomplete_OperCd.as_view(), name='Autocomplete_OperCd'),
    path('Autocomplete_DataList/', views.Autocomplete_DataList.as_view(), name='Autocomplete_DataList'),
    path('Autocomplete_DBOwner/', views.Autocomplete_DBOwner.as_view(), name='Autocomplete_DBOwner'),
    path('Autocomplete_StdDomainType/', views.Autocomplete_StdDomainType.as_view(), name='Autocomplete_StdDomainType'),
    path('Autocomplete_TableList/', views.Autocomplete_TableList.as_view(), name='Autocomplete_TableList'),
    path('Autocomplete_TableList_Meta/', views.Autocomplete_TableList_Meta.as_view(), name='Autocomplete_TableList_Meta'),
    path('Autocomplete_DomainAndDbList/', views.Autocomplete_DomainAndDbList.as_view(), name='Autocomplete_DomainAndDbList'),
    path('Autocomplete_DBTablespace/', views.Autocomplete_DBTablespace.as_view(), name='Autocomplete_DBTablespace'),
    path('Autocomplete_MetaGrantList/', views.Autocomplete_MetaGrantList.as_view(), name='Autocomplete_MetaGrantList'),
    path('Autocomplete_MetaReq_User_Search/', views.Autocomplete_MetaReq_User_Search.as_view(), name='Autocomplete_MetaReq_User_Search'),
    path('Autocomplete_ProjectList/', views.Autocomplete_ProjectList.as_view(), name='Autocomplete_ProjectList'),
    path('Autocomplete_MetaReq_DbList/', views.Autocomplete_MetaReq_DbList.as_view(), name='Autocomplete_MetaReq_DbList'),
    # path('Autocomplete_DbOwner/', views.Autocomplete_DbOwner.as_view(), name='Autocomplete_DbOwner'),



    ###########################################################################
    ## AJAX
    ###########################################################################
    path('ajaxOneDBMonitorLV/', views.ajaxOneDBMonitorLV, name='ajaxOneDBMonitorLV'),
    path('ajaxExecuteSQL/', views.ajaxExecuteSQL, name='ajaxExecuteSQL'),
    path('ajaxShowClickedSQL/', views.ajaxShowClickedSQL, name='ajaxShowClickedSQL'),
    path('ajaxMetaDataDetail/', views.ajaxMetaDataDetail, name='ajaxMetaDataDetail'),
    path('ajaxDomain/', views.ajaxDomain, name='ajaxDomain'),
    path('ajaxOtherSaveNameSQL/', views.ajaxOtherSaveNameSQL, name='ajaxOtherSaveNameSQL'),
    path('ajaxDeleteSQL/', views.ajaxDeleteSQL, name='ajaxDeleteSQL'),
    path('ajaxSearchKeywordAutoComplete/', views.ajaxSearchKeywordAutoComplete, name='ajaxSearchKeywordAutoComplete'),
    path('ajaxShareSQL/', views.ajaxShareSQL, name='ajaxShareSQL'),
    path('ajaxUserRequestWord/', views.ajaxUserRequestWord, name='ajaxUserRequestWord'),
    path('ajaxUserRequestData/', views.ajaxUserRequestData, name='ajaxUserRequestData'),
    path('ajaxRequestTuning/', views.ajaxRequestTuning, name='ajaxRequestTuning'),
    
    path('ajaxTuningListDVModifyTuningStatus/', views.ajaxTuningListDVModifyTuningStatus, name='ajaxTuningListDVModifyTuningStatus'),

    path('ajaxDataview/', views.ajaxDataview, name='ajaxDataview'),
    path('ajaxDataviewClick/', views.ajaxDataviewClick, name='ajaxDataviewClick'),
    path('ajaxDataviewExecuteSQL/', views.ajaxDataviewExecuteSQL, name='ajaxDataviewExecuteSQL'),
    path('ajaxReqestPriv/', views.ajaxReqestPriv, name='ajaxReqestPriv'),
    path('ajaxExecuteUserPriv/', views.ajaxExecuteUserPriv, name='ajaxExecuteUserPriv'),
    path('ajaxExecuteUserActivation/', views.ajaxExecuteUserActivation, name='ajaxExecuteUserActivation'),
    path('ajaxExecuteUserDrop/', views.ajaxExecuteUserDrop, name='ajaxExecuteUserDrop'),
    path('ajaxCheckTabPriv/', views.ajaxCheckTabPriv, name='ajaxCheckTabPriv'),
    path('ajaxExecuteMeta/', views.ajaxExecuteMeta, name='ajaxExecuteMeta'),
    path('ajaxModifyMeta/', views.ajaxModifyMeta, name='ajaxModifyMeta'),
    path('ajaxCreateUserFromSabun/', views.ajaxCreateUserFromSabun, name='ajaxCreateUserFromSabun'),
    path('ajaxCreateUser/', views.ajaxCreateUser, name='ajaxCreateUser'),
    path('ajaxDivAttr/', views.ajaxDivAttr, name='ajaxDivAttr'),
    path('ajaxMetaRegShowColumn/', views.ajaxMetaRegShowColumn, name='ajaxMetaRegShowColumn'),
    path('ajaxMetaRegCheckColumn/', views.ajaxMetaRegCheckColumn, name='ajaxMetaRegCheckColumn'),
    path('ajaxMetaReqSave/', views.ajaxMetaReqSave, name='ajaxMetaReqSave'),
    path('ajaxMetaReqUpdate/', views.ajaxMetaReqUpdate, name='ajaxMetaReqUpdate'),
    path('ajaxMetaLoadReq/', views.ajaxMetaLoadReq, name='ajaxMetaLoadReq'),
    path('ajaxGetDBMSCase/', views.ajaxGetDBMSCase, name='ajaxGetDBMSCase'),
    path('ajaxMetaReqOK/', views.ajaxMetaReqOK, name='ajaxMetaReqOK'),
    path('ajaxMetaCancel/', views.ajaxMetaCancel, name='ajaxMetaCancel'),
    path('ajaxMetaCreate/', views.ajaxMetaCreate, name='ajaxMetaCreate'),
    # path('ajaxMetaCreateColumnDdl/', views.ajaxMetaCreateColumnDdl, name='ajaxMetaCreateColumnDdl'),
    path('ajaxMetaAlter/', views.ajaxMetaAlter, name='ajaxMetaAlter'),
    path('ajaxSaveDbaScript/', views.ajaxSaveDbaScript, name='ajaxSaveDbaScript'),
    path('ajaxDbAlertOff/', views.ajaxDbAlertOff, name='ajaxDbAlertOff'),
    path('ajaxDatabaseDetail/', views.ajaxDatabaseDetail, name='ajaxDatabaseDetail'),
    path('ajaxAllExecuteSql/', views.ajaxAllExecuteSql, name='ajaxAllExecuteSql'),
    path('ajaxRequestNewAttr/', views.ajaxRequestNewAttr, name='ajaxRequestNewAttr'),
    path('ajaxSelectWord/', views.ajaxSelectWord, name='ajaxSelectWord'),
    path('ajaxSelectDomain/', views.ajaxSelectDomain, name='ajaxSelectDomain'),
    path('ajaxRequestNewWord/', views.ajaxRequestNewWord, name='ajaxRequestNewWord'),    
    path('ajaxRequestStdModify/', views.ajaxRequestStdModify, name='ajaxRequestStdModify'),
    path('ajaxRequestNewDomain/', views.ajaxRequestNewDomain, name='ajaxRequestNewDomain'),    
    path('ajaxGetDupTable/', views.ajaxGetDupTable, name='ajaxGetDupTable'),
    path('ajaxMetaHandWork/', views.ajaxMetaHandWork, name='ajaxMetaHandWork'),
    path('ajaxViewColumnDetail/', views.ajaxViewColumnDetail, name='ajaxViewColumnDetail'),
    path('ajaxCreateDDLLVErd/', views.ajaxCreateDDLLVErd, name='ajaxCreateDDLLVErd'),
    path('ajaxCreateDDLLVExcel/', views.ajaxCreateDDLLVExcel, name='ajaxCreateDDLLVExcel'),
    path('ajaxCreateDDLLVErdDownload/', views.ajaxCreateDDLLVErdDownload, name='ajaxCreateDDLLVErdDownload'),
    path('ajaxCreateDDLLVErdChangeDownload/', views.ajaxCreateDDLLVErdChangeDownload, name='ajaxCreateDDLLVErdChangeDownload'),
    path('ajaxCreateDDLLVHtmlChangeDownload/', views.ajaxCreateDDLLVHtmlChangeDownload, name='ajaxCreateDDLLVHtmlChangeDownload'),
    
    path('ajaxDatabaseListSyncWithGoogleSheet/', views.ajaxDatabaseListSyncWithGoogleSheet, name='ajaxDatabaseListSyncWithGoogleSheet'),

    ###########################################################################
    ## excel download
    ###########################################################################
    # url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
    url(r'^export/xls/$', views.DataViewExportData, name='DataViewExportData'),

    # path('dataSearchKeywordDetail/<int:column_id>/<int:data_type>', views.dataSearchKeywordDetail, name='dataSearchKeywordDetail'),
    # path('dataSearchCategory/<int:column_id>/<int:domain_id>/<int:data_type>', views.dataSearchCategory, name='dataSearchCategory'),
    # path('dataSQL/', views.dataSQL, name='dataSQL'),
    # path('dataSearchFlow/', views.dataSearchFlow, name='dataSearchFlow'),
    # path('dataSearch/', views.dataSearch, name='dataSearch'),

    ###########################################################################
    ## Chart
    ###########################################################################
    path('chart_team_visit_cnt/', views.chart_team_visit_cnt, name='chart_team_visit_cnt'),
    path('chart_db_size/', views.chart_db_size, name='chart_db_size'),
    # path('chart_monitor/', views.chart_monitor, name='chart_monitor'),

    path('ApiTest/', views.ApiTest.as_view(), name='ApiTest'),
] 