from django.shortcuts import render
from django.template import Context, loader


# Create your views here.
import logging
logger = logging.getLogger(__name__)
from django.db import connections
from django.conf import settings
from django.shortcuts import redirect
from .models import *

from django.shortcuts import render_to_response, render
from django.template import RequestContext



def base(request) :
	return render(request, 'base.html')

	


# def index(request) :
# 	# Login 한 user 만 접속 허용
# 	# Login 페이지를 통하지 않았을 경우 Login 페이지로 redirect
# 	if not request.user.is_authenticated :
# 		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

# 	template_parent = "dashboard"

# 	return render(request, 'index.html', {
# 													'template_parent':template_parent
# 												})

