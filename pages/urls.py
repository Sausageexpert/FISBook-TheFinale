from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home,name='home'),
    path('explore/',views.explore,name='explore'),
    path('user/<slug:reg_no>',views.user,name='user'),
    path('explore/get/<str:forum>', views.get, name='get')
]