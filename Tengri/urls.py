from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<str:pk>', views.news, name='news'),
    path('search_articles', views.search_articles, name='search_articles'),
    path('sorted_articles', views.sorted_articles, name='sorted_articles')
]
