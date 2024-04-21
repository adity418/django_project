from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email")

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


    