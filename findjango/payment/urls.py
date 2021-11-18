from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('purchaseoption/', views.purchasing_option, name='purchasing_option'),
    path('process/<int:id>/', views.payment_process, name='process'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('done/', views.payment_done, name='done'),
]