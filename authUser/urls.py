from django.urls import path

from authUser import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="sign-up"),
    path("login/", views.LoginView.as_view(), name="login"),
    # path("just/", views.just.as_view(), name="just")
    # logut
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/<int:pk>", views.Settings.as_view(), name="settings"),
    path("change-password/",
         views.PasswordChange.as_view(), name="change-password"),
    path("user", views.UserView.as_view(), name="user"),
    path("post-details/<int:pk>", views.PostDetails.as_view(), name="postdetails"),
    path("d/", views.DummYView.as_view(), name="d"),
    path("c/", views.CView.as_view(), name="c"),

]
