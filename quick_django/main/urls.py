from django.urls import path
from . import views

# ルーティング情報を列挙する
urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
    path('iftag', views.iftag, name='iftag'),
    path('yesno', views.yesno, name='yesno'),
    path('firstof', views.firstof, name='firstof'),
    path('forloop', views.forloop, name='forloop'),
    path('forempty', views.forempty, name='forempty')
]
