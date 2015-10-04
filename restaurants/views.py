# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def menu(request):
	foods = [
		{'name':'蕃茄炒蛋', 'price' : 60, 'comment' : '好吃', 'is_spicy' : False},
		{'name':'蒜泥白肉', 'price' : 60, 'comment' : '人氣推薦', 'is_spicy' : True}
	]

	return render_to_response('menu.html', locals())
