from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("mypage/", views.mypage, name="mypage"),
    path("profile/", views.profile_edit, name="profile_edit"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
