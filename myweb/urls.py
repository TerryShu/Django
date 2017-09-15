"""mblog URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainsite.views import homepage, showpost , listing , about , disp_detail,show_try ,tvshow,FBLogin,talk,talklist,mail,diary

urlpatterns = [
<<<<<<< HEAD
    url(r'^diary/',diary),
=======
    url(r'^diary',diary),
>>>>>>> 7d8f841ba0f1f80bf236287ce5c9645d0b0a6e17
    url(r'^mail/', mail),
    url(r'^talk/', talk),
    url(r'^talklist/', talklist),
    url(r'^fb/', FBLogin),
	url(r'^tv/(\d{1})$', tvshow , name='tv_url'),
    url(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})$', show_try),
    url(r'^post/(\w+)$', showpost),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^list/([0-9a-zA-Z]+)', disp_detail),
	url(r'^list/', listing),
    url(r'^about/', about),
	url(r'^$', homepage),
]
