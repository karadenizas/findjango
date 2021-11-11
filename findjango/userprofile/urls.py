from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
]