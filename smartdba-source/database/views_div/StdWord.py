# # -*-coding: utf-8-*-

# from database.views.common import *

# # 단어 첫 화면 진입
# class StdWordLV(LoginRequiredMixin, FormMixin, ListView) :

#   model = StdWord
#   template_name = 'StdWordLV.html'
#   context_object_name = 'objects'
#   paginate_by = 10
#   form_class = StdWordForm
#   keyword = ""

#   # 신청된 단어 리스트
#   def get_context_data(self, **kwargs):

#       context = super().get_context_data(**kwargs)     

#       req_word = StdWord.objects.filter(accept_yn__gt=0,
#                                         reg_dtm__gt=datetime.datetime.now() - datetime.timedelta(days=5)).order_by('-reg_dtm','std_wd_kor')      

#       context['template_parent'] = "stddata"
#       context['template_child'] = "StdWordLV"
#       context['req_word'] = req_word

#       return context

# # 키워드 입력, 조회 시
# def ajaxSelectWord(request) :
  
#   std_wd_kor = request.POST.get('word','')
#   choice_tab_or_col = request.POST.get('choice_tab_or_col','')

#   obj = []

#   word_data = []

#   if choice_tab_or_col == "1" :
#     qs1 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_kor__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_kor',)
#     qs2 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_kor__icontains=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                     *( (~Q(std_wd_kor__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_kor',)

    
#     obj = list(chain(qs1, qs2))

#     for data in obj :
#       word_data.append( [
#           data.std_wd_kor.replace(std_wd_kor,'<b><font color=red>'+std_wd_kor+'</font></b>'),
#           data.std_wd_eng,
#           data.std_wd_eng_ful,
#           data.expl,
#           ]
#       )


#   elif choice_tab_or_col == "2" :

#     qs1 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_eng__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_eng',)
#     qs2 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_eng__icontains=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                     *( (~Q(std_wd_eng__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_eng',)

#     obj = list(chain(qs1, qs2))

#     for data in obj :
#       word_data.append( [
#           data.std_wd_kor,
#           data.std_wd_eng.replace(std_wd_kor,'<b><font color=red>'+std_wd_kor+'</font></b>'),
#           data.std_wd_eng_ful,
#           data.expl,
#           ]
#       )

#   elif choice_tab_or_col == "3" :

#     qs1 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_eng_ful__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_eng_ful',)
#     qs2 =  StdWord.objects.filter(
#                                     *( (Q(std_wd_eng_ful__icontains=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                     *( (~Q(std_wd_eng_ful__iexact=std_wd_kor.upper(),accept_yn=0),) if std_wd_kor  else ()),
#                                      ).order_by('std_wd_eng_ful',)

#     obj = list(chain(qs1, qs2))


#     for data in obj :
#       word_data.append( [
#           data.std_wd_kor,
#           data.std_wd_eng,
#           data.std_wd_eng_ful.replace(std_wd_kor,'<b><font color=red>'+std_wd_kor+'</font></b>'),
#           data.expl,
#           ]
#       )

#   context = {
#              'word_data':word_data,
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")     


# # 새로운 단어 요청
# def ajaxRequestNewWord(request) :
  
#   std_wd_kor = request.POST.get('std_wd_kor','')
#   std_wd_eng = request.POST.get('std_wd_eng','')
#   std_wd_eng_ful = request.POST.get('std_wd_eng_ful','')
#   expl = request.POST.get('expl','')

#   std_wd_kor = std_wd_kor.upper()
#   std_wd_eng = std_wd_eng.upper()
#   std_wd_eng_ful = std_wd_eng_ful.upper()

#   error_msg = ""

#   chk_dup_eng = StdWord.objects.filter( ~Q(std_wd_kor=std_wd_kor),
#                                          Q(std_wd_eng=std_wd_eng),
#                                          accept_yn="0"
#                                       )

#   if chk_dup_eng  :
#     chk_dup_eng = chk_dup_eng[0]
#     error_msg = "오류 : 영문약어명이 중복됩니다. 다른 중복 약어를 입력해주세요<br>* 중복단어 : {std_wd_kor} / {std_wd_eng}".format(std_wd_kor=chk_dup_eng.std_wd_kor,
#                                                                                                             std_wd_eng=chk_dup_eng.std_wd_eng)

#   else :
    
#     obj, flag = StdWord.objects.get_or_create(
#                                                 std_wd_kor = std_wd_kor,
#                                               )

#     if flag : ## 생성
#       obj.std_wd_eng = std_wd_eng
#       obj.std_wd_eng_ful = std_wd_eng_ful
#       obj.expl = expl
#       obj.reg_dtm = datetime.datetime.now()
#       obj.id_reg_user = request.user
#       obj.accept_yn = 1

#       obj.save()
#     else : # 존재
#       # 반려
#       if obj.accept_yn == "2" :
#         obj.std_wd_eng = std_wd_eng
#         obj.std_wd_eng_ful = std_wd_eng_ful
#         obj.expl = expl
#         obj.reg_dtm = datetime.datetime.now()
#         obj.id_reg_user = request.user
#         obj.accept_yn = 1
#         obj.reject_exp = ""

#         obj.save()
#       else :
#         error_msg = "오류 : [{std_wd_kor}]는 이미 존재하는 단어입니다.".format(std_wd_kor=std_wd_kor)


#   context = {
#              'result':'OK',
#              'error_msg':error_msg
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json") 


# # 단어/도메인/용어 승인/반려/취소
# def ajaxRequestStdModify(request) :

#   req_id = request.POST.get('req_id','')
#   # 0 : 단어
#   # 1 : 도메인
#   # 2 : 용어
#   std_div = request.POST.get('std_div','')
#   req_div = request.POST.get('req_div','')
#   comment = request.POST.get('comment','')

#   print(req_id)
#   print(std_div)
#   print(req_div)
#   print(comment)



#   error_yn = "N"
#   error_msg = ""

#   if std_div == "0"  : # 단어
#     if req_div == "1" : # 취소
#       data = StdWord.objects.get(id=req_id).delete()
#       error_msg = "정상적으로 취소되었습니다."

#     elif req_div == "0" : # 승인
#       data = StdWord.objects.get(id=req_id)
#       data.accept_yn = "0"
#       data.reject_exp = "승인되었습니다" if comment == "" else comment

#       data.save()

      
#       print(data.id_reg_user.username)
#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       print(1)
#       msg = """[SmartDBA] 단어 "{nm}" 가 승인 되었습니다""".format(nm=data.std_wd_kor)
#       print(2)
#       query_sms(ds_emp['MOBILE'],msg)
#       print(3)

#       error_msg = "정상적으로 승인되었습니다."
      

#     elif req_div == "2" : # 반려
#       data = StdWord.objects.get(id=req_id)
#       data.accept_yn = "2"
#       data.reject_exp = comment
#       data.save()

#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       msg = """[SmartDBA] 단어 "{nm}" 가 반려 되었습니다""".format(nm=data.std_wd_kor)
#       query_sms(ds_emp['MOBILE'],msg)

#       error_msg = "정상적으로 반려되었습니다."

#   elif std_div == "1"  : # 도메인
#     if req_div == "1" : # 취소
#       data = StdDomain.objects.get(id=req_id).delete()
#       error_msg = "정상적으로 취소되었습니다."

#     elif req_div == "0" : # 승인
#       data = StdDomain.objects.get(id=req_id)

#       id_reg_user = data.id_reg_user
#       id_stddomain = data
#       domain_name = data.domain_name


#       data.accept_yn = "0"
#       data.reject_exp = "승인되었습니다" if comment == "" else comment
#       data.save()


#       if domain_name[-2:] in ('코드','번호') :
#         l_lkor, \
#         l_leng, \
#         l_domain, \
#         l_eng_attr_name, \
#         l_domain_flag, \
#         l_word_find_flag, \
#         l_last_num_flag, \
#         lcnt, \
#         total_attr, \
#         max_length, \
#         l_attr_find, \
#         l_aleary_req, \
#         list_attr =  f_div_attr(domain_name)

#         ok_div = l_word_find_flag[0]

#         attr_div_eng = '_'.join(l_leng[0])


#         if ok_div :
#           attr_data = StdAttr(
#                   id_stddomain = id_stddomain,
#                   std_attr_kor = domain_name,
#                   std_attr_eng = attr_div_eng,
#                   reg_dtm = datetime.datetime.now(),
#                   id_reg_user = id_reg_user,
#                   accept_yn = 0,
#                   use_yn=1
#                 )
#           attr_data.save()

#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       msg = """[SmartDBA] 도메인 "{nm}" 가 승인 되었습니다""".format(nm=data.domain_name)
#       query_sms(ds_emp['MOBILE'],msg)


#       error_msg = "정상적으로 승인되었습니다."

#     elif req_div == "2" : # 반려
#       data = StdDomain.objects.get(id=req_id)
#       data.accept_yn = "2"
#       data.reject_exp = comment
#       data.save()

#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       msg = """[SmartDBA] 도메인 "{nm}" 가 반려 되었습니다""".format(nm=data.domain_name)
#       query_sms(ds_emp['MOBILE'],msg)

#       error_msg = "정상적으로 반려되었습니다."

#   elif std_div == "2"  : # 용어
#     if req_div == "1" : # 취소
#       data = StdAttr.objects.get(id=req_id).delete()
#       error_msg = "정상적으로 취소되었습니다."

#     elif req_div == "0" : # 승인
#       data = StdAttr.objects.get(id=req_id)
#       data.accept_yn = "0"
#       data.reject_exp = "승인되었습니다" if comment == "" else comment
#       data.save()

#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       msg = """[SmartDBA] 용어 "{nm}" 가 승인 되었습니다""".format(nm=data.std_attr_kor)
#       query_sms(ds_emp['MOBILE'],msg)

#       error_msg = "정상적으로 승인되었습니다."

#     elif req_div == "2" : # 반려
#       data = StdAttr.objects.get(id=req_id)
#       data.accept_yn = "2"
#       data.reject_exp = comment
#       data.save()

#       error_msg = "정상적으로 반려되었습니다."

#       ds_emp = query_dict('iam',iamSql.format(emp_no=data.id_reg_user.username))[0]
#       msg = """[SmartDBA] 용어 "{nm}" 가 반려 되었습니다""".format(nm=data.std_attr_kor)
#       query_sms(ds_emp['MOBILE'],msg)



#   context = {
#              'result':'OK',
#              'error_yn': error_yn,
#              'error_msg':error_msg
#             }

#   param = json.dumps(context, default=json_default)

#   return HttpResponse(param, content_type="application/json")