from django.shortcuts import render
from users.forms import CustomUserCreation
from django.views.generic.edit import CreateView
from users.models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreation