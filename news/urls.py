from django import views
from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.news),
    re_path(r'^(?P<year>\d+)/(?P<month>\d+)/', views.news),
    re_path(r'^(?P<year>\d+)/', views.news),
    re_path(r'^$', views.news),
]
