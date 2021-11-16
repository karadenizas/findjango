from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('', views.purchasing_option, name='purchasing_option'),
]