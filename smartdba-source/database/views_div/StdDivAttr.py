# # -*-coding: utf-8-*-

# from database.views.common import *

# class StdDivAttrLV(LoginRequiredMixin, FormMixin, ListView) :

#   model = StdWord
#   template_name = 'StdDivAttrLV.html'
#   context_object_name = 'objects'
#   form_class = StdWordForm

#   def get_queryset(self):

#     self.form = self.get_form(self.form_class)
#     obj = []
#     return obj

#   def post(self, request, *args, **kwargs) :

#     return self.get(request, *args, **kwargs)

#   def get_context_data(self, **kwargs):

      
#       loggingVisit(self.request, 19)

#       context = super().get_context_data(**kwargs)

#       req_attr = StdAttr.objects.filter(accept_yn__gt=0,                                        
#                                         reg_dtm__gt=datetime.datetime.now() - datetime.timedelta(days=5)).order_by('-reg_dtm')

#       context['template_parent'] = "stddata"
#       context['template_child'] = "StdDivAttrLV"
#       context['req_attr'] = req_attr

#       return context


# # 용어 나누기 클릭
# def ajaxDivAttr(request) :

#   loggingVisit(request, 27)

#   attr = request.POST.get('attr','')
#   attr = attr.upper()

#   clean_attr = (attr.replace('[','')).replace(']','')
  
#   qs1 = StdAttr.objects.filter(std_attr_kor__iexact=clean_attr,accept_yn=0,use_yn=1)
#   qs2 = StdAttr.objects.filter(std_attr_kor__icontains=clean_attr,accept_yn=0,use_yn=1).order_by('std_attr_kor')



#   exact_datatype = ""

#   print(qs1)
#   if len(qs1) > 0 :
#     exact_datatype = qs1[0].id_stddomain.info_type
#     print(exact_datatype)




#   dataset = qs1.union(qs2)


#   attr_data = []



#   final_data_type = []

#   for data in dataset :
#     if data.std_attr_kor == clean_attr :
#         sql = """SELECT {id} ID, data_type DATA_TYPE, count(*) CNT
#                   FROM CUST_COLUMN_LIST
#                   WHERE COLUMN_NAME = '{column_name}'
#                   AND DATA_TYPE = '{data_type}'
#                   AND DB_USE = 'SMTC'
#                   AND DROP_YN = 0
#                   group by data_type
#                   order by 2 desc
#               """.format(column_name=data.std_attr_eng,
#                          data_type=data.id_stddomain.oracle_datatype,
#                          id=data.id)

#         cnt_ds = query_dict("default", sql)

#         if len(cnt_ds) > 0 :
#           final_data_type.append([cnt_ds[0]['ID'],cnt_ds[0]['CNT'],len(cnt_ds[0]['DATA_TYPE'])])

#   if len(final_data_type) > 0 :
#     final_data_type = sorted(final_data_type, key=itemgetter(1,2), reverse=True)

#     final_data_type_id = final_data_type[0][0]

#     in_dataset = StdAttr.objects.get(id=final_data_type_id)

#     attr_data.append(
#       [
#         in_dataset.std_attr_kor.replace(clean_attr,'<b><font color=red>'+clean_attr+'</font></b>'),
#         in_dataset.std_attr_eng,
#         f_get_datatype(in_dataset.id,'ORACLE'),
#         f_get_datatype(in_dataset.id,'MYSQL'),
#         in_dataset.id_stddomain.info_type,
#         in_dataset.expl,
#       ]
#     )

#   for data in dataset :
#     if data.std_attr_kor != clean_attr :
#       attr_data.append(
#         [
#           data.std_attr_kor.replace(clean_attr,'<b><font color=red>'+clean_attr+'</font></b>'),
#           data.std_attr_eng,
#           f_get_datatype(data.id,'ORACLE'),
#           f_get_datatype(data.id,'MYSQL'),
#           data.id_stddomain.info_type,
#           data.expl,
#         ]
#       )

#   l_lkor, \
#   l_leng, \
#   l_domain, \
#   l_eng_attr_name, \
#   l_domain_flag, \
#   l_word_find_flag, \
#   l_last_num_flag, \
#   lcnt, \
#   total_attr, \
#   max_length, \
#   l_attr_find, \
#   l_aleary_req, \
#   list_attr =  f_div_attr(attr)

#   context = {
#              'lkor':l_lkor,
#              'leng':l_leng,
#              'domain':l_domain,
#              'eng_attr_name':l_eng_attr_name,
#              'domain_flag':l_domain_flag,
#              'word_find_flag':l_word_find_flag,
#              'last_num_flag':l_last_num_flag,
#              'lcnt':lcnt,
#              'total_attr':total_attr,
#              'max_length':max_length,
#              'list_attr':list_attr,
#              'l_attr_find':l_attr_find,
#              'l_aleary_req':l_aleary_req,
#              'attr_data':attr_data,
#              'exact_datatype':exact_datatype
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")



# def ajaxRequestNewAttr(request) :
#   id_stddomain = request.POST.get('id_stddomain','')
#   kor = request.POST.get('kor','')
#   eng = request.POST.get('eng','')
#   csr_no = request.POST.get('csr_no','')

#   error_msg = ""

#   obj, flag = StdAttr.objects.get_or_create(
#                                               std_attr_kor = kor,
#                                               std_attr_eng = eng,
#                                               id_stddomain = StdDomain.objects.get(id=id_stddomain),                                              
#                                               use_yn=1,
#                                             )

#   if flag : ## 생성
#     obj.id_stddomain = StdDomain.objects.get(id=id_stddomain)
#     obj.reg_dtm = datetime.datetime.now()
#     obj.csr_no = csr_no
#     obj.id_reg_user = request.user
#     obj.accept_yn = 1

#     obj.save()
#   else : # 존재
#     # 반려 중일 경우
#     if obj.accept_yn == 2 :
#       obj.id_stddomain = StdDomain.objects.get(id=id_stddomain)
#       obj.reg_dtm = datetime.datetime.now()
#       obj.csr_no = csr_no
#       obj.id_reg_user = request.user
#       obj.accept_yn = 1
#       obj.reject_exp = ""

#       obj.save()
#     else :
#       error_msg = "* 오류 : 이미 [{username}]에 의해 신청되었으며, 승인 대기 중입니다.".format(username=obj.id_reg_user.first_name)

#   context = {
#              'result':'OK',
#              'error_msg':error_msg
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")  