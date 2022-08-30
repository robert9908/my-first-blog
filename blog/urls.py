from django.urls import path
from . import view
surlpatterns = [
    path('', views.post_list, name='post_list'),
]