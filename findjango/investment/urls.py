from django.urls import path
from . import views

app_name = 'invest'

urlpatterns = [
    path('create/', views.create_form, name='create_invest'),
]