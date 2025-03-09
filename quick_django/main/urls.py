from django.urls import path
from . import views

# ルーティング情報を列挙する
urlpatterns = [
    path('', views.index, name='index')
]
