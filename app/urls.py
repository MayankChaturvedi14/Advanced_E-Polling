from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("",views.index,name='home'),
    path("join",views.join,name='join'),
    path("faq",views.faq,name='faq'),
    path("about",views.about,name='about'),
    path("ad",views.ad,name='ad'),
    path("list",views.list,name='list'),
    path("result",views.result,name='result'),
    path("cn",views.cn,name='cn'),
    path("main",views.main,name='main'),
]
