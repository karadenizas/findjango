from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('htmx-latest-advices/', views.htmx_latest_advices),
    path('htmx-popular-advices/', views.htmx_popular_advices),
]