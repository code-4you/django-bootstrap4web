# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
	"""
		Default page to connect
	"""
	return render (request, 'site/index.html',{})

def edit(request):
	"""
		Edit page
	"""
	return render (request, 'site/edit.html',{})

def insert(request):
	"""
		Insert page when you do
	"""
	return render (request, 'site/insert.html',{})

