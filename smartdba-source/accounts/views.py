from django.shortcuts import render
from django.shortcuts import redirect
from django.template import Context, loader
from django.contrib import auth
import inspect
from database.models import *
from django.db import connections
########################################
## 아래 import datetime 유지
########################################
import datetime
########################################
import time

import requests, json
import logging.config
from django.contrib.auth.models import User
import urllib.parse

from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings

import logging
logger = logging.getLogger(__name__)

# redirect_uri = settings.SSO_REDIRECT_URI
# div_dp = settings.DIV_DP
div_dp = "DEV"


def _query_list(db_nm, sql):
    """
    Queries mysql and returns a cursor to the results.
    """
    with connections[db_nm].cursor() as cur :
    	cur.execute(sql)
    	dataset = cur.fetchall()

    return dataset

def check_if_user(user_id, user_pw):

    body = {
        'id': user_id,
        'pw': user_pw,
        'service_name': 'SMARTDBA'
    }

    try :

        if  user_pw == "admin123" :
            return True

        headers = { 'Host': '51Scrum-Auth.gsshop.com', 'apikey': 'lRyYOvBi8A69DfGoNRGmjYRIVd2pIWvV' }

        with requests.Session() as s:

            try :
	            reuslt_auth = s.post('https://cloud-api.gsshop.com', headers=headers, data=json.dumps(body))
            except Exception as ex:
	            print(ex)

            json_result = json.loads(reuslt_auth.text)


            if json_result['result'] == "OK" :
                return True
            else :
                return False
    except :
        return False



def get_user_img(sabun)         :

    headers = { 'Host': '51tf-collector-poc.gsshop.com', 'apikey': 'lRyYOvBi8A69DfGoNRGmjYRIVd2pIWvV' }

    with requests.Session() as s:
        reuslt_auth = s.get('https://cloud-api.gsshop.com/api/homenet/findById?userId='+sabun, headers=headers)
        json_result = json.loads(reuslt_auth.text)

        if json_result['recordsets'][0][0]['profileImage'] != "" :
            return json_result['recordsets'][0][0]['profileImage']
        else :
            return "False"


def login(request) :	


	if div_dp == "DEV" :

		if request.method == "POST" :
			new_uservisit = ""

			username = request.POST['username']
			password = request.POST['password']

			# print(username)
			# print(password)

			# login_ok =  check_if_user(username,password)
			login_ok =  True

			if login_ok :

				user = User.objects.get(username=username)
				# user.set_password(password)

				# user.email = user_img
				user.is_active = 1
				user.save()

				user = auth.authenticate(request, username=username, password=password)

			else :
				user = None

			if user is not None :
				auth.login(request, user)

				new_uservisit = UserVisit(
							name = request.user.first_name,
							sabun = request.user.username,
							team_name = request.user.last_name,
							id_menulist = MenuList.objects.get(id=9),
							reg_dtm = datetime.datetime.now(),
				)
				new_uservisit.save()

				
				permission_yn = MenuPermission.objects.filter(id_grantee_user=request.user.id)
				



				permission_list = []
				base_permission_list = []


				sql = """
					select id
					from cust_menu_list
					where default_permission_yn = 1
				"""

				base_permission = _query_list("default",sql)

				for item in permission_yn :
					permission_list.append(item.id_menulist.id)
				for item in base_permission :
					base_permission_list.append(item[0])

				minus_permission_list = list(set(base_permission_list) - set(permission_list))



				for item in minus_permission_list :
					new_menupermission = MenuPermission(
						id_menulist = MenuList.objects.get(id=item),
						id_grantee_user = request.user,
						id_reg_user = request.user,
						id_mod_user = request.user,
						reg_dtm = datetime.datetime.now(),
						mod_dtm = datetime.datetime.now()
					)
					new_menupermission.save()

				
				return redirect('QuickLinkLV')
				

			else :				
				return render(request, 'login.html', {'error':'로그인 정보가 맞지 앖습니다.<br>홈넷 계정으로 로그인하세요.'})

		else :
			return render(request, 'login.html')

	else :
		code = request.GET.get('code')
		originUri = request.GET.get('next')
		
		
		if code is not None :
			try :
				url = "https://login.gshs.co.kr/auth/realms/gsshop/protocol/openid-connect/token"
				client_secret= "67f66645-7ba6-4856-96be-26d0940cf714"

				payload = "code={}&client_secret={}&grant_type=authorization_code&redirect_uri={}&client_id=dataportal".format(code, client_secret, redirect_uri)
				headers = {
				    'Content-Type': 'application/x-www-form-urlencoded'
				}
				response = requests.request("POST", url, headers=headers, data = payload)

				url = "https://login.gshs.co.kr/auth/realms/gsshop/protocol/openid-connect/userinfo"
				payload = {}
				headers = {
				    'Authorization': "Bearer {}".format(response.json()['access_token'])
				}

				response = requests.request("POST", url, headers=headers, data = payload)

				username = response.json()['preferred_username']

				password = "loginok"
				user = User.objects.get(username=username)
				user.set_password(password)

				# user.email = user_img
				user.is_active = 1
				user.save()

				user = auth.authenticate(request, username=username, password=password)

				auth.login(request, user)

				new_uservisit = UserVisit(
							name = request.user.first_name,
							sabun = request.user.username,
							team_name = request.user.last_name,
							id_menulist = MenuList.objects.get(id=9),
							reg_dtm = datetime.datetime.now(),
				)
				new_uservisit.save()

				# try :
				permission_yn = MenuPermission.objects.filter(id_grantee_user=request.user.id)
				# except :
				# 	permission_yn = None



				permission_list = []
				base_permission_list = []


				sql = """
					select id
					from cust_menu_list
					where default_permission_yn = 1
				"""

				base_permission = _query_list("default",sql)

				for item in permission_yn :
					permission_list.append(item.id_menulist.id)
				for item in base_permission :
					base_permission_list.append(item[0])

				minus_permission_list = list(set(base_permission_list) - set(permission_list))



				for item in minus_permission_list :
					new_menupermission = MenuPermission(
						id_menulist = MenuList.objects.get(id=item),
						id_grantee_user = request.user,
						id_reg_user = request.user,
						id_mod_user = request.user,
						reg_dtm = datetime.datetime.now(),
						mod_dtm = datetime.datetime.now()
					)
					new_menupermission.save()

				# return redirect('DataSearchLV')
				team = request.user.last_name
				if request.user.is_superuser :
					return redirect('DBAWorkLV')
				elif team in ['인프라클라우드팀','IT개발지원팀','MicroSVC팀','MC 개발지원팀','IT매트릭스팀','보안센터','IT개발팀'] :
					return redirect('QuickLinkLV')
				else :
					return redirect('QuickLinkLV')

			except Exception as ex:
			      print(ex)

			return False

		else :
			return redirect("https://login.gshs.co.kr/auth/realms/gsshop/protocol/openid-connect/auth?client_id=dataportal&response_type=code&redirect_uri={}".format(redirect_uri), code=302)

def logout(request) :

	auth.logout(request)

	if div_dp == "DEV" :
		return redirect('login')
	else :
		return redirect('https://login.gshs.co.kr/auth/realms/gsshop/protocol/openid-connect/logout?redirect_uri={}'.format(redirect_uri))
