import os
from django.shortcuts import render, redirect
from .models import Video
from django.conf import settings
from .utils import upload_to_s3
from courses.models import Course
from django.contrib.auth.decorators import user_passes_test
from edu_connate.utils import is_admin
# Create your views here.

@user_passes_test(is_admin)
def add_video(request):
    courses = Course.objects.all()
    if request.method == 'POST' and  request.FILES.get('video_file'):
        video_file = request.FILES['video_file']
        file_extension = os.path.splitext(video_file.name)[1]
        title = request.POST['title']
        selected_course = request.POST['course']
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME  # Your S3 bucket name
        file_path = f"videos/{title}{file_extension}"  # Path in the bucket

        if not title or not video_file:
            return render(request, 'videos/add_video.html', {'error': 'Both title and video are required', 'courses': courses})

        video_url = upload_to_s3(video_file, bucket_name, file_path)
        course = Course.objects.get(id=selected_course)
        Video.objects.create(
            title=title,
            user=request.user,
            s3_key=video_url,
            course=course
        )

        return render(request, 'videos/add_video.html', {'success': 'Video Added Successfully', 'courses': courses})

    print(courses)
    return render(request, 'videos/add_video.html', {'courses': courses})
