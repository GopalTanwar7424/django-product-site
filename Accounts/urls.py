from django.urls import path 
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.login, name='sigin'),
    path('logout/', views.logout, name='logout'),
]
