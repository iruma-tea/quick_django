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
    path('forempty', views.forempty, name='forempty'),
    path('fortag', views.fortag, name='fortag'),
    path('ifchanged', views.ifchanged, name='ifchanged'),
    path('regroup', views.regroup, name='regroup'),
    path('cycle', views.cycle, name='cycle'),
    path('escape', views.escape, name='escape'),
    path('temptag', views.temptag, name='temptag'),
    path('verbatim', views.verbatim, name='verbatim'),
    path('master', views.master, name='master'),
    path('include', views.include, name='include'),
    path('static', views.static, name='static'),
    path('strformat', views.strformat, name='strformat'),
    path('slice', views.slice, name='slice'),
    path('date_time', views.date_time, name='date_time'),
    path('filter', views.filter, name='filter'),
    path('exclude', views.exclude, name='exclude'),
    path('get', views.get, name='get'),
    path('filter_or', views.filter_or, name='filter_or'),
    path('filter_other', views.filter_other, name='filter_other'),
    path('groupby', views.groupby, name='groupby'),
    path('union', views.union, name='union'),
    path('raw', views.raw, name='raw'),
    path('rel', views.rel, name='rel'),
    path('rel2', views.rel2, name='rel2'),
    path('route_param/<int:id>', views.route_param, name='route_param'),
]
