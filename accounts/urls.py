from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=EmailAuthenticationForm  # ← ここで指定
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
     path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
    path("register/", views.register, name="register"),
    path("mypage/", views.mypage, name="mypage"),
    path("profile/", views.profile_edit, name="profile_edit"),
]
