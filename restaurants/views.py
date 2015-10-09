# -*- coding: utf-8 -*-
##from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.sessions.models import Session
from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm
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
	request.session['restaurants'] = restaurants
	return render_to_response('restaurants_list.html', locals())

def comment(request, id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect('/restaurants_list/')

	if request.POST:
		f = CommentForm(request.POST)
		if f.is_valid():
			visitor = f.cleaned_data['visitor']
			content = f.cleaned_data['content']
			email = f.cleaned_data['email']
			date_time = timezone.localtime(timezone.now())

			c = Comment.objects.create(
				visitor = visitor,
				email = email,
				content = content,
				data_time = date_time,
				request = r
			)

		f = CommentForm(initial = {'content' : '我沒意見'})
	return render_to_response('comments.html', RequestContext(request, locals()))

def set_c(request):
	response = HttpResponse('Set your lucky_number as 8')
	response.set_cookie('lucky_number', 8)
	return response

def use_session(request):
    request.session['lucky_number'] =  8
    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']
        response = HttpResponse('Your lucky number is {0}'.format(lucky_number))

    del request.session['lucky_number']

    return response

def use_session2(request):
    #sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk = sid2)

    s_info = 'Session ID:' + sid2 + '<br/>SessionID2:' + sid2 + '<br/>Expire_date: ' + str(s.expire_date) + '<br/>Data: ' + str(s.get_decoded())

    return HttpResponse(s_info)