from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_staff", "is_active", "role")  
    search_fields = ("email", "username")

admin.site.register(User, CustomUserAdmin)