from django.http import HttpResponse
from django.urls import path 

urlpatterns = [
    path('', lambda request: HttpResponse("Users Home Page"))
]