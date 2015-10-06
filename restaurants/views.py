# -*- coding: utf-8 -*-
##from django.shortcuts import render
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food
# Create your views here.

def menu(request):
	##foods = [
	##	{'name':'蕃茄炒蛋', 'price' : 60, 'comment' : '好吃', 'is_spicy' : False},
	##	{'name':'蒜泥白肉', 'price' : 60, 'comment' : '人氣推薦', 'is_spicy' : True}
	##]
	path = request.path
	restaurants = Restaurant.objects.all()
	return render_to_response('menu.html', locals())

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html', locals())