from typing import Any
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

from authUser.models import CustomUser
from myblogapp.models import BlogUploader
from .forms import RegisterForm, LoginForm, UserEditForm, UserChangePasswordForm
from django.views.generic import FormView, CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from django.contrib.auth import login, logout, authenticate
# Create your views here.


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "html/userauth/sign.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# @user_passes_test(user_check)
# def just(req):
#     print(req.user.user_choice)
#     return render(req, "html/index.html")


class LoginView(FormView):
    form_class = LoginForm
    template_name = "html/userauth/login.html"
    success_url = reverse_lazy("index")
    print("******************* uppwer form ***************")

    def form_valid(self, form):
        print("form vald ")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Authentication failed, redirect back to login page
            return redirect("sign-in")


# def user_check(user):
#     return user.user_choices

# @method_decorator(user_passes_test(user_check, login_url="login"), name="dispatch")
# class just(TemplateView):
#     template_name = "html/index.html"


class Settings(UpdateView):
    template_name = "html/userauth/settings.html"
    form_class = UserEditForm
    success_url = reverse_lazy("index")
    model = CustomUser

    def get_template_names(self):
        if self.request.user.user_choice == "Content Creator":
            return ["html/userauth/settings.html"]
        else:
            return [self.template_name]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordChange(PasswordChangeView):
    template_name = "html/userauth/password.html"
    success_url = reverse_lazy("index")


class DummYView(TemplateView):
    template_name = "admin_page/index.html"


class CView(TemplateView):
    template_name = "admin_page/charts.html"


class PostDetails(DetailView):
    template_name = "html/userauth/post-details.html"
    model = BlogUploader
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        getId = self.kwargs.get("pk")
        customUser = get_object_or_404(CustomUser, id=getId)
        postdetails = BlogUploader.objects.filter(author=customUser)
        context["postDetails"] = postdetails
        return context


class UserView(View):
    def get(self, req, *args, **kwargs):
        if req.user.user_choice == "Content Creator":
            return render(req, "html/userauth/content.html")
        else:
            return render(req, "html/userauth/settings.html")
