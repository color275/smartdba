# # -*-coding: utf-8-*-

# from database.views.common import *



# class TuningListLV(LoginRequiredMixin, FormMixin, ListView) :


#   model = TuningList
#   template_name = 'TuningListLV.html'
#   context_object_name = 'objects'
#   form_class = TuningListLVForm
#   paginate_by = 10

#   def get_initial(self):

#     ###################################################
#     ## 화면에 바인딩 된 값을 유지하기 위한 처리
#     ###################################################
#     title = ""

#     keyword = self.request.session['keyword'] if 'keyword' in self.request.session else ""
#     id_dblist = self.request.session['id_dblist'] if 'id_dblist' in self.request.session else ""
#     id_domain = self.request.session['id_domain'] if 'id_domain' in self.request.session else ""
#     id_projectlist = self.request.session['id_projectlist'] if 'id_projectlist' in self.request.session else ""
#     id_tuningstatus = self.request.session['id_tuningstatus'] if 'id_tuningstatus' in self.request.session else ""
#     choice_status = self.request.session['choice_status'] if 'choice_status' in self.request.session else ""


#     return {
#                   'keyword': keyword,
#                   'id_dblist': id_dblist,
#                   'id_domain': id_domain,
#                   'id_projectlist': id_projectlist,
#                   'id_tuningstatus': id_tuningstatus,
#                   'choice_status': choice_status,
#             }


#   def get_queryset(self):

#     self.form = self.get_form(self.form_class)

#     keyword = self.request.POST.get('keyword','')




#     if self.form.is_valid():

#       id_dblist = self.form.cleaned_data['id_dblist']
#       id_domain = self.form.cleaned_data['id_domain']
#       id_projectlist = self.form.cleaned_data['id_projectlist']
#       id_tuningstatus = self.form.cleaned_data['id_tuningstatus']
#       choice_status = self.form.cleaned_data['choice_status']


#       ###################################################
#       ## 화면에 바인딩 된 값을 유지하기 위한 처리
#       ###################################################
#       self.request.session['keyword'] = keyword if keyword is not None else ""
#       self.request.session['id_dblist'] = id_dblist.id if id_dblist is not None else ""
#       self.request.session['id_domain'] = id_domain.id if id_domain is not None else ""
#       self.request.session['id_projectlist'] = id_projectlist.id if id_projectlist is not None else ""
#       self.request.session['id_tuningstatus'] = id_tuningstatus.id if id_tuningstatus is not None else ""
#       self.request.session['choice_status'] = choice_status if choice_status is not None else ""


#       ###################################################
#       ## SEARCH 버튼 클리 시 페이징이 1번으로 가기 위한 코드
#       ###################################################
#       self.request.session['click_search'] = 'Y'
#       ###################################################

#     else :
#       ###################################################
#       ## 1. 처음 진입
#       ## 2. 페이징 버튼 클릭 시
#       ###################################################

#       page_kwarg = self.page_kwarg
#       page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
#       if page == 1 :
#         self.request.session['keyword'] = ""
#         self.request.session['id_dblist'] = ""
#         self.request.session['id_domain'] = ""
#         self.request.session['id_projectlist'] = ""
#         self.request.session['id_tuningstatus'] = ""
#         self.request.session['choice_status'] = ""

#       keyword = self.request.session['keyword'] if 'keyword' in self.request.session else ""
#       id_dblist = self.request.session['id_dblist'] if 'id_dblist' in self.request.session else ""
#       id_domain = self.request.session['id_domain'] if 'id_domain' in self.request.session else ""
#       id_projectlist = self.request.session['id_projectlist'] if 'id_projectlist' in self.request.session else ""
#       id_tuningstatus = self.request.session['id_tuningstatus'] if 'id_tuningstatus' in self.request.session else ""
#       choice_status = self.request.session['choice_status'] if 'choice_status' in self.request.session else ""

#     loggingVisit(self.request, 13)

#     if choice_status == '' :
#       if keyword.isdigit() :
#         obj =  TuningList.objects.exclude(id=999999999).filter(
#                                                                 (
#                                                                  Q(id=int(keyword))
#                                                                  ),
#                                                                 *( (Q(id_dblist=id_dblist),) if id_dblist  else ()),
#                                                                 *( (Q(id_domain=id_domain),) if id_domain  else ()),
#                                                                 *( (Q(id_projectlist=id_projectlist),) if id_projectlist  else ()),
#                                                                 *( (Q(id_tuningstatus=id_tuningstatus),) if id_tuningstatus  else ()),
#                                                               ).order_by("-id")
#       else :
#         obj =  TuningList.objects.exclude(id=999999999).filter(
#                                                                 (Q(title__icontains=keyword)|
#                                                                  Q(id_reg_user__first_name=keyword)
#                                                                  ),
#                                                                 *( (Q(id_dblist=id_dblist),) if id_dblist  else ()),
#                                                                 *( (Q(id_domain=id_domain),) if id_domain  else ()),
#                                                                 *( (Q(id_projectlist=id_projectlist),) if id_projectlist  else ()),
#                                                                 *( (Q(id_tuningstatus=id_tuningstatus),) if id_tuningstatus  else ()),
#                                                               ).order_by("-id")
#     elif choice_status == '1' : # SQL ID 검색
#       obj =  TuningList.objects.exclude(id=999999999).filter(
#                                                               (Q(sql_id__icontains=keyword)),
#                                                               *( (Q(id_dblist=id_dblist),) if id_dblist  else ()),
#                                                               *( (Q(id_domain=id_domain),) if id_domain  else ()),
#                                                               *( (Q(id_projectlist=id_projectlist),) if id_projectlist  else ()),
#                                                               *( (Q(id_tuningstatus=id_tuningstatus),) if id_tuningstatus  else ()),
#                                                             ).order_by("-id")
#     elif choice_status == '2' : # TUNNING TEXT 검색
#       obj =  TuningList.objects.exclude(id=999999999).filter(
#                                                               (  Q(asis_sql_text__icontains=keyword)|
#                                                                  Q(tobe_sql_text__icontains=keyword)
#                                                                  ),
#                                                               *( (Q(id_dblist=id_dblist),) if id_dblist  else ()),
#                                                               *( (Q(id_domain=id_domain),) if id_domain  else ()),
#                                                               *( (Q(id_projectlist=id_projectlist),) if id_projectlist  else ()),
#                                                               *( (Q(id_tuningstatus=id_tuningstatus),) if id_tuningstatus  else ()),
#                                                             ).order_by("-id")




#     return obj


#   def post(self, request, *args, **kwargs) :
#     return self.get(request, *args, **kwargs)

#   def paginate_queryset(self, queryset, page_size):

#         paginator = self.get_paginator(
#             queryset, page_size, orphans=self.get_paginate_orphans(),
#             allow_empty_first_page=self.get_allow_empty())
#         page_kwarg = self.page_kwarg
#         page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
#         try:
#             page_number = int(page)
#         except ValueError:
#             if page == 'last':
#                 page_number = paginator.num_pages
#             else:
#                 raise Http404(_("Page is not 'last', nor can it be converted to an int."))
#         try:

#             ###################################################
#             ## SEARCH 버튼 클릭 시 페이징이 1번으로 가기 위한 코드
#             ###################################################
#             if 'click_search' in self.request.session :
#               if self.request.session['click_search'] == "N" :
#                 page = paginator.page(page_number)
#               else :
#                 page = paginator.page(1)
#             else :
#               page = paginator.page(page_number)
#             ###################################################


#             ###################################################
#             ## COLUMNLIST 에서 목록으로 클릭 시 원래 페이지 번호를 찾아가기 위한 코드
#             ###################################################
#             self.request.session['page_number'] = page_number

#             return (paginator, page, page.object_list, page.has_other_pages())



#         except :
#           page = paginator.page(1)
#           return (paginator, page, page.object_list, page.has_other_pages())

#   def get_context_data(self, **kwargs):



#       context = super().get_context_data(**kwargs)

#       page_range = ""
#       paginator = context['paginator']
#       page_numbers_range = 5  # Display only 5 page numbers
#       max_index = len(paginator.page_range)

#       ###################################################
#       ## SEARCH 버튼 클리 시 페이징이 1번으로 가기 위한 코드
#       ###################################################
#       if 'click_search' in self.request.session :
#         if self.request.session['click_search'] == "N" :
#           page = self.request.GET.get('page')
#         else :
#           page = 1
#           self.request.session['click_search'] = "N"
#       else :
#         page = self.request.GET.get('page')
#       ###################################################


#       current_page = int(page) if page else 1

#       start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#       end_index = start_index + page_numbers_range
#       if end_index >= max_index:
#         end_index = max_index

#       page_range = paginator.page_range[start_index:end_index]
#       context['page_range'] = page_range

#       context['template_parent'] = "TuningListLV"
#       context['template_child'] = "TuningListLV"

#       return context



# # class TuningListDV(LoginRequiredMixin, DetailView) :

# #   model = TuningList
# #   template_name = 'TuningListDV.html'
# #   context_object_name = 'objects'


# #   def get_object(self):
# #       tuninglist = get_object_or_404(TuningList, id=self.kwargs['id'])

# #       return tuninglist

# #   def get_context_data(self, **kwargs):

# #       loggingVisit(self.request, 13)

# #       dba_member = User.objects.filter(is_superuser="1")
# #       dba_users = []

# #       for m in dba_member :
# #         dba_users.append(m.id)



# #       context = super().get_context_data(**kwargs)

# #       context['template_parent'] = "TuningListLV"
# #       context['template_child'] = "TuningListLV"
# #       context['dba_users'] = dba_users

# #       return context

# class TuningListCV(LoginRequiredMixin, CreateView):



#   model = TuningList
#   form_class = TuningListForm
#   template_name = 'TuningListCV.html'

#   # success_url = reverse_lazy('sqlTuningMain')

#   def get_success_url(self):
#     return reverse_lazy('TuningListDV', kwargs={'id': self.object.id })

#   def get_form_kwargs(self):
#       # add request for form to validate
#       kwargs = super().get_form_kwargs()
#       kwargs.update({"request": self.request})
#       return kwargs

#   def get_context_data(self, **kwargs):

#       loggingVisit(self.request, 13)


#       context = super(CreateView, self).get_context_data(**kwargs)

#       context['template_parent'] = "TuningListLV"
#       context['template_child'] = "TuningListLV"
#       context['dba_users'] = "dba_users"

#       return context

# class TuningListUV(LoginRequiredMixin, UpdateView):

#   model = TuningList
#   form_class = TuningListForm
#   template_name = 'TuningListUV.html'

#   context_object_name = 'objects'


#   def get_success_url(self):

#     return reverse_lazy('TuningListDV', kwargs={'id': self.object.id })


#   def get_object(self):
#           obj = get_object_or_404(TuningList, id=self.kwargs['id'])

#           return obj

#   def get_form_kwargs(self):
#       # add request for form to validate
#       kwargs = super().get_form_kwargs()
#       kwargs.update({"request": self.request})
#       return kwargs

#   def get_context_data(self, **kwargs):

#       loggingVisit(self.request, 13)

#       context = super().get_context_data(**kwargs)

#       context['template_parent'] = "TuningListLV"
#       context['template_child'] = "TuningListLV"

#       return context


# class TuningListDeleteView(LoginRequiredMixin, DeleteView) :

#   model = TuningList
#   success_message='Your Photo has been deleted successfully.'

#   def get_success_url(self):
#     return reverse_lazy('TuningListLV')      


# class TuningListDV(LoginRequiredMixin, FormMixin, DetailView) :

#   model = TuningList
#   template_name = 'TuningListDV.html'
#   context_object_name = 'objects'
#   form_class = TuningListDVForm


  
#   def get_object(self):
#       tuninglist = get_object_or_404(TuningList, id=self.kwargs['id'])

#       return tuninglist

#   # form 에 request 를 넘겨준다
#   def get_form_kwargs(self):
#       # add request for form to validate
#       kwargs = super().get_form_kwargs()
#       kwargs.update({"request": self.request})
#       kwargs.update({"obj_id": self.kwargs['id']})
#       return kwargs

#   def post(self, request, *args, **kwargs) :
#     return self.get(request, *args, **kwargs)

#   def get_context_data(self, **kwargs):

#       loggingVisit(self.request, 13)

#       dba_member = User.objects.filter(is_superuser="1")
#       dba_users = []

#       for m in dba_member :
#         dba_users.append(m.id)

#       context = super().get_context_data(**kwargs)

#       context['template_parent'] = "TuningListLV"
#       context['template_child'] = "TuningListLV"
#       context['dba_users'] = dba_users

#       return context    

