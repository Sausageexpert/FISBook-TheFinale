from django.urls import path,include
from . import views

app_name='forums'

urlpatterns = [
    path('forums/<str:forum_id>',views.forum,name='forum'),
    path('event/<int:event_id>',views.event,name='event'),
    path('forums/<int:forum_id>/members',views.member_list,name='member_list'),
    path('makeforum',views.makeforum,name='makeforum'),
    path('test', views.test, name='test')
]

