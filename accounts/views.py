from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserProfileCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from members.models import Subscription

def register(request):
    if request.method == "POST":
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)  # ← これを追加（自動ログイン）
            messages.success(request, f"{user.username} さん、登録が完了しました！")
            return redirect("top")
    else:
        form = UserProfileCreationForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def add_review(request, store_id):
    pass

@login_required
def mypage(request):
    return render(request, "accounts/mypage.html")

@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("top")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_edit.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"{form.get_user().username} さん、ログインしました！")
        return super().form_valid(form)

    def get_success_url(self):
        return "/"  # ログイン後はトップへ
    
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "ログアウトしました。")
        return super().dispatch(request, *args, **kwargs)
    
def subscription(request):
    return render(request, "accounts/subscription.html")