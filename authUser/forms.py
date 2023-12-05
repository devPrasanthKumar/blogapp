from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "user_choice"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class UserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "user_choice"]


class UserChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]
