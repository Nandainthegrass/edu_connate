from django.http import HttpResponse
from django.urls import path
from .views import add_course

urlpatterns = [
    path('', lambda request: HttpResponse("Courses Home Page")),
    path('add-course/', add_course)
]