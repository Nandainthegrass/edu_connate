from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from edu_connate.utils import is_admin
from .models import Course

# Create your views here.
@user_passes_test(is_admin)
def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        num_hours = request.POST.get('num_hours')
        description = request.POST.get('description', 'This course has no description')

        if not name or not num_hours:
            return render(request, 'courses/add_course.html', {'error': 'Name and number of hours are required'})

        try:
            num_hours = int(num_hours)
        except ValueError:
            return render(request, 'courses/add_course.html', {'error': 'Number of hours must be an integer'})

        Course.objects.create(name=name, num_hours=num_hours, description=description)

        return redirect('course_list')

    return render(request, 'courses/add_course.html')

@user_passes_test(is_admin)
def show_all_courses_and_videos(request):
    return 