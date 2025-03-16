from django.http import HttpResponse
from django.urls import path 
from .views import add_video

urlpatterns = [
    path('add-video/', add_video),
]