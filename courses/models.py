from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    num_hours = models.IntegerField()
    description = models.TextField(default="This course has no description")
    num_students = models.PositiveIntegerField(default=0)