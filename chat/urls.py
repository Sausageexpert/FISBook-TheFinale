from django.urls import path
from . import views

urlpatterns = [
    path('checkForRoom/', views.checkForRoom, name='checkForRoom'),
    path('<str:room>/', views.room, name='room'),
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    path('get/<str:room>/', views.get, name='get'),
]
