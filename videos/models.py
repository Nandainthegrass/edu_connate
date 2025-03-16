from django.db import models
from users.models import User
from courses.models import Course

class Video(models.Model):
    title = models.CharField(max_length=255)
    s3_key = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
