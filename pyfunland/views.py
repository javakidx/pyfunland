# -*- coding: utf-8 -*-
from django.http import HttpResponse

def here(request):
	#return HttpResponse('Mom, I am here!')
	return HttpResponse('媽，我在這！')

def add(request, a, b):
	total = int(a) + int(b)
	return HttpResponse(str(total));