from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('user/<str:slug>', views.user_profile, name='user_profile'),
]