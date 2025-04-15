from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('news-detail/', views.news_detail, name="news-detail")
]