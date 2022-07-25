from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

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
    path("logout",views.SignOut,name="logout"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
