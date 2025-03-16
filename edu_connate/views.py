from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

User = get_user_model()

# Register View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = 'student'  # Default to student

        user = User.objects.create_user(username=username, password=password, role=role)
        user.save()
        messages.success(request, 'User registered successfully!')
        return redirect('login')
    return render(request, 'auth/register.html')
    
# Login View
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'auth/login.html')

# Logout View
def logout_user(request):
    logout(request)
    return redirect('login')
