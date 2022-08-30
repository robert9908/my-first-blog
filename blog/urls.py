from django.urls import path
from blog import views
surlpatterns = [
    path('', views.post_list, name='post_list'),
]