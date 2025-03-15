from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [("student", "Student"), ("admin", "Admin")]
   
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    #relationship -- django will create a table.
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"