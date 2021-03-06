"""funland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pyfunland.views import here
from pyfunland.views import add
from pyfunland.views import math
from pyfunland.views import welcome

from restaurants.views import menu, list_restaurants, comment, set_c, use_session, use_session2


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', add),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),

    url(r'^menu/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
	url(r'^test_cookie/$', set_c),
    url(r'^test_session/$', use_session),
    url(r'^test_session2/$', use_session2)
]
