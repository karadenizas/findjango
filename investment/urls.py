from django.urls import path
from . import views

app_name = 'invest'

urlpatterns = [
    path('create/', views.create_form, name='create_invest'),
    path('preview/<int:id>', views.preview_invest, name='preview_invest'),
    path('review/<int:id>', views.review_invest, name='review_invest'),
    path('htmx-latest-rate/', views.htmx_latest_rate),
    path('htmx-create-invest/', views.htmx_create_invest),
]