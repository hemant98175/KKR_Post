# created by me - Hemant

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('postnew', views.postnew),
    path('post', views.post_question),
    path('reply', views.reply),
    path('postanswere', views.postanswere),
    path('view_reply', views.view_reply),
    path('registration', views.registration),





]
