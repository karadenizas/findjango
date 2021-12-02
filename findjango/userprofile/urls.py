from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('account/', views.account_settings, name='account_settings'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('settings/done/', views.profile_change_done, name='profile_change_done'),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('register/done/', views.register_done, name='register_done'),
    path('user/<str:slug>', views.user_profile, name='user_profile'),
]