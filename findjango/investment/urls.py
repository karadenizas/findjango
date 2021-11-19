from django.urls import path
from . import views

app_name = 'invest'

urlpatterns = [
    path('create/', views.create_form, name='create_invest'),
    path('preview/<int:id>', views.preview_invest, name='preview_invest'),
    path('review/<int:id>', views.review_invest, name='review_invest'),
]