# # -*-coding: utf-8-*-

# from database.views.common import *



# class StdDomainLV(LoginRequiredMixin, FormMixin, ListView) :

#   model = StdDomain
#   template_name = 'StdDomainLV.html'
#   context_object_name = 'objects'
#   paginate_by = 10
#   form_class = StdDomainForm
#   keyword = ""

#   def get_context_data(self, **kwargs):      
#       context = super().get_context_data(**kwargs)
      

#       # 반려건 조회
#       req_domain = StdDomain.objects.filter(accept_yn__gt=0,
#                                             reg_dtm__gt=datetime.datetime.now() - datetime.timedelta(days=5)).order_by('domain_name')    

#       context['template_parent'] = "stddata"
#       context['template_child'] = "StdDomainLV"
#       context['req_domain'] = req_domain      

#       return context


# # 키워드 조회
# def ajaxSelectDomain(request) :

#   domain_name = request.POST.get('word','')  
#   id_std_domaintype = request.POST.get('id_id_std_domaintype','')

#   obj = []
#   word_data = []


#   if len(domain_name) > 0 or len(id_std_domaintype) :

# 	  qs1 =  StdDomain.objects.filter( Q(accept_yn=0),
# 	                                   Q(use_yn=1),
# 	                                  *( (Q(domain_name__iexact=domain_name.upper()),) if domain_name  else ()),
# 	                                  *( (Q(id_std_domaintype=id_std_domaintype),) if id_std_domaintype  else ()),
# 	                                   ).order_by('domain_name',)
# 	  qs2 =  StdDomain.objects.filter( Q(accept_yn=0),
# 	                                   Q(use_yn=1),
# 	                                  *( (Q(domain_name__icontains=domain_name.upper()),) if domain_name  else ()),
# 	                                  *( (~Q(domain_name__iexact=domain_name.upper()),) if domain_name  else ()),
# 	                                  *( (Q(id_std_domaintype=id_std_domaintype),) if id_std_domaintype  else ()),
# 	                                   ).order_by('domain_name',)

# 	  obj = list(chain(qs1, qs2))

# 	  for data in obj :
# 	    word_data.append( [
# 	        data.domain_name.replace(domain_name.upper(),'<b><font color=red>'+domain_name.upper()+'</font></b>'),
# 	        data.info_type,
# 	        data.oracle_datatype,
# 	        data.mysql_datatype,
# 	        data.expl,
# 	        ]
# 	    )

#   context = {
#              'word_data':word_data,
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")


# def ajaxRequestNewDomain(request) :
#   id_domain_name = request.POST.get('id_domain_name','')
#   id_data_type_text = request.POST.get('id_data_type_text','')
#   id_data_type_value = request.POST.get('id_data_type_value','')
#   id_leng = request.POST.get('id_leng','')
#   id_decimal_leng = request.POST.get('id_decimal_leng','')
#   id_group_code = request.POST.get('id_group_code','')
#   id_group_code_yn_value = request.POST.get('id_group_code_yn_value','')
#   expl = request.POST.get('id_expl','')


#   error_msg = ""
#   ok_div = True
#   attr_div = ""

#   if id_domain_name[-2:] in ('코드','번호') :
#     l_lkor, \
#     l_leng, \
#     l_domain, \
#     l_eng_attr_name, \
#     l_domain_flag, \
#     l_word_find_flag, \
#     l_last_num_flag, \
#     lcnt, \
#     total_attr, \
#     max_length, \
#     l_attr_find, \
#     l_aleary_req, \
#     list_attr =  f_div_attr(id_domain_name)

#     ok_div = l_word_find_flag[0]
#     attr_div = ' '.join(l_lkor[0])


#     if ok_div == False :
#       error_msg = "* 오류 : 구성 단어가 없습니다. [ " + attr_div + " ]"

#     if StdAttr.objects.filter(std_attr_kor=id_domain_name,use_yn=1).exists() :
#       ok_div = False
#       error_msg = "* 오류 : 동일한 이름의 용어가 존재합니다. [ " + attr_div + " ]"


#   else :
#     if StdWord.objects.filter(std_wd_kor=id_domain_name).exists() == False :
#       ok_div = False
#       error_msg = "* 오류 : 등록된 단어가 아닙니다. 단어를 먼저 신청해주세요. [ " + id_domain_name + " ]"




#   if ok_div :

#     oracle_datatype = ""

#     # 1 : 문자열
#     if id_data_type_value == "1" and int(id_leng) <= 4000:
#       oracle_datatype = "VARCHAR2(" + id_leng + ")"
#     # 2 : 숫자
#     elif id_data_type_value == "2" :
#       oracle_datatype = "NUMBER" + \
#                         ( "(" + str(id_leng) if id_leng != "" else ""  ) + \
#                         ( "," + str(id_decimal_leng) if id_decimal_leng != "" else "" ) +  \
#                         ( ")" if id_leng != "" else ""  )
#     # 3 : 날짜
#     elif id_data_type_value == "3" :
#       oracle_datatype = "DATE"

#     elif id_data_type_value == "1" and int(id_leng) > 4000:
#       oracle_datatype = 'CLOB'
#     else :
#       oracle_datatype = id_data_type_text


#     mysql_datatype = ""

#     # 1 : 문자열
#     if id_data_type_value == "1" and int(id_leng) <= 16000:
#       mysql_datatype = "VARCHAR(" + id_leng + ")"
#     # 2 : 숫자
#     elif id_data_type_value == "2" :
#       if id_decimal_leng != "" :
#         mysql_datatype = "DECIMAL"
#       elif id_leng != "" and int(id_leng) >= 1 and int(id_leng) < 3 :
#         mysql_datatype = "TINYINT"
#       elif id_leng != "" and int(id_leng) >= 3 and int(id_leng) < 5 :
#         mysql_datatype = "SMALLINT"
#       elif id_leng != "" and int(id_leng) >= 5 and int(id_leng) < 9 :
#         mysql_datatype = "INT"
#       elif id_leng != "" and int(id_leng) >= 9 and int(id_leng) < 19 :
#         mysql_datatype = "BIGINT"
#       elif id_leng != "" and int(id_leng) >= 19 :
#         mysql_datatype = "DECIMAL"
#     # 3 : 날짜
#     elif id_data_type_value == "3" :
#       mysql_datatype = "DATETIME"
#     elif id_data_type_value == "1" and int(id_leng) > 16000:
#       mysql_datatype = 'TEXT'
#     else :
#       mysql_datatype = id_data_type_text


#     data_type = id_domain_name + "_" + id_data_type_text + str(id_leng) + ( "," + str(id_decimal_leng) if id_decimal_leng != "" else "" )


#     obj, flag = StdDomain.objects.get_or_create(
#                                                 info_type = data_type,
#                                               )


#     if flag : ## 생성
#       obj.domain_name = id_domain_name
#       obj.id_stddatatype = StdDataType.objects.get(id=id_data_type_value)
#       obj.oracle_datatype = oracle_datatype
#       obj.mysql_datatype = mysql_datatype
#       obj.group_code = id_group_code
#       obj.group_code_yn = id_group_code_yn_value
#       obj.expl = expl
#       obj.reg_dtm = datetime.datetime.now()
#       obj.id_reg_user = request.user
#       obj.accept_yn = 1

#       obj.save()
#     else : # 존재
#       # 반려상태에서 다시 신청할 경우
#       if obj.accept_yn == "2" :
#         obj.domain_name = id_domain_name
#         obj.id_stddatatype = StdDataType.objects.get(id=id_data_type_value)
#         obj.oracle_datatype = oracle_datatype
#         obj.mysql_datatype = mysql_datatype
#         obj.group_code = id_group_code
#         obj.group_code_yn = id_group_code_yn_value
#         obj.expl = expl
#         obj.reg_dtm = datetime.datetime.now()
#         obj.id_reg_user = request.user
#         obj.accept_yn = 1
#         obj.reject_exp = ""

#         obj.save()
#       else :
#         error_msg = "* 오류 : 이미 존재하는 도메인입니다."

#   context = {
#              'result':'OK',
#              'error_msg':error_msg
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")  


# class Autocomplete_StdDomainType(autocomplete.Select2QuerySetView):
#   def get_queryset(self):
#     # Don't forget to filter out results depending on the visitor !
#     if not self.request.user.is_authenticated :
#       return StdDomainType.objects.none()
#     qs = StdDomainType.objects.all().order_by('domain_type')
#     if self.q:
#       qs = qs.filter(domain_type__contains=self.q.upper())
#     return qs  