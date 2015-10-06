# -*- coding: utf-8 -*-
from django.http import HttpResponse
###from django.template.loader import get_template
###from django import template
from django.shortcuts import render_to_response

def here(request):
	#return HttpResponse('Mom, I am here!')
	return HttpResponse('媽，我在這！')

def add(request, a, b):
	total = int(a) + int(b)
	return HttpResponse(str(total));

def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	#t = template.Template('<html>sum={{s}}<br/>dif={{d}}<br/>pro={{p}}<br/>quo={{q}}</html>')
	##with open('templates/math.html', 'r') as reader:
	##	t = template.Template(reader.read())
	###t = get_template('math.html');
	###c = template.Context({'s' : s, 'd' : d, 'p' : p, 'q' : q})

	###return HttpResponse(t.render(c))
	####return render_to_response('math.html', {'s' : s, 'd' : d, 'p' : p, 'q' : q});
	return render_to_response('math.html', locals())


def menu(request):
	foods = [{
			'name' : '蕃茄炒蛋',
			'price' : 60,
			'comment' : '好吃',
			'is_spicy' : False
		},
		{
			'name' : '蒜泥白肉',
			'price' : 100,
			'comment' : '人氣推薦',
			'is_spicy' : True
		}
	]
	return render_to_response('menu.html', locals())

def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] != '':
		return HttpResponse('Welcome!~' + request.GET['user_name'])
	else:
		return render_to_response('welcome.html', locals())