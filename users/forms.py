from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "birth_date",
            "password1",
            "password2",
        )

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "birth_date",
        )
