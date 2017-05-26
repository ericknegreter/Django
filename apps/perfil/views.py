# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext

# Create your views here.

def login_views(request):
	return render(request, 'public/sign-in.html')
	#return HttpResponse("login")

def register_views(request):
	return render(request, 'public/sign-up.html')
	#return HttpResponse("registro")