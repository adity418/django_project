from django.contrib import admin
from users.models import CustomUser
from users.forms import CustomUserChange, CustomUserCreation
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomUser
    list_display = ["email", "username"]

admin.site.register(CustomUser, CustomUserAdmin)