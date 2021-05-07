"""audio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from music_api.views import DetailApiView,UpdateApiView,CreateApiView,DeleteApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^item/(?P<slug>[-\w]+)(?:/(?P<pk>[0-9]+))?/$', DetailApiView.as_view(),name='DetailApiView'),
    re_path(r'^update/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', UpdateApiView.as_view(),name='UpdateApiView'),
    re_path(r'^create/$', CreateApiView.as_view(),name='CreateApiView'),
    re_path(r'^delete/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', DeleteApiView.as_view(),name='DeleteApiView'),

]
