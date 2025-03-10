from django.urls import path
from . import views

# ルーティング情報を列挙する
urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
]
