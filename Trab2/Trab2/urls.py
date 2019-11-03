"""Trab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin 
from MyBay.views import register, home, viewproduct, edit_profile, deleteaccount, editproduct, deleteproduct, change_password, myproducts, createproduct, searchproducts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^myacccount/$', edit_profile, name='view_profile'),
    url(r'^password/$', change_password, name='change_password'),
    url(r'^myproducts/$', myproducts, name='myproducts'),
    url(r'^(?P<id>\d+)/edit/$', editproduct, name='editproduct'),
    url(r'^(?P<id>\d+)/deleteproduct/$', deleteproduct, name='deleteproduct'),
    url(r'^createproduct/$', createproduct, name='createproduct'),
    url(r'^(?P<id>\d+)/viewproduct/$', viewproduct, name='viewproduct'),
    url(r'^deleteaccount/$', deleteaccount, name='deleteaccount'),    
    url(r'^searchproducts/$', searchproducts, name='searchproducts'),
    url(r'^register/$', register, name='register'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
