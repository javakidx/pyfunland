# -*- coding: utf-8 -*-
##from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
# Create your views here.

def menu(request):
	##foods = [
	##	{'name':'蕃茄炒蛋', 'price' : 60, 'comment' : '好吃', 'is_spicy' : False},
	##	{'name':'蒜泥白肉', 'price' : 60, 'comment' : '人氣推薦', 'is_spicy' : True}
	##]
	path = request.path
	####restaurants = Restaurant.objects.all()
	restaurant = Restaurant.objects.get(id=1)
	return render_to_response('menu.html', locals())

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html', locals())

def comment(request, id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect('/restaurants_list/')

	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		email = request.POST['email']
		date_time = timezone.localtime(timezone.now())
		
		Comment.objects.create(
			visitor = visitor,
			content = content,
			email = email,
			date_time = date_time,
			restaurant = r
		)
	return render_to_response('comments.html', RequestContext(request, locals()))

