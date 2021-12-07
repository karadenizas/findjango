from django.urls import path
from . import views

app_name = 'result'

urlpatterns = [
    path('', views.result_index, name='result_index'),
    path('detail/<int:id>/', views.result_detail, name='result_detail'),
]