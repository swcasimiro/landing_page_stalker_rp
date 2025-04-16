from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views
from rest_framework import routers
from .viewset import NewsViewSet


router = DefaultRouter()
router.register(r'news', NewsViewSet)


urlpatterns = [
    path('', views.news, name='news'),
    path('<slug:slug>', views.news_detail, name="news-detail"),
    path('api/', include(router.urls)),
]