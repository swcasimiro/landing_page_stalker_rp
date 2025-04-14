from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('policy/', views.policy, name='policy'),
    path('rules/', views.rules, name='rules'),
    path('rules_project/', views.rules_project, name='rules_project')
]