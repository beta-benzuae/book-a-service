from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from web import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    path('output/', views.redirect, name="redirect"),

]