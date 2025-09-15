from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserProfileCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.views import LoginView
from members.models import Subscription

def register(request):
    if request.method == "POST":
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← これを追加（自動ログイン）
            return redirect("mypage")
    else:
        form = UserProfileCreationForm()
    return render(request, "accounts/register.html", {"form": form})

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
            return redirect("mypage")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_edit.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        user = self.request.user
        # 有料プラン未加入なら subscription ページへ
        if not Subscription.objects.filter(user=user, is_active=True).exists():
            return "/members/subscription/"
        # 加入済みなら mypage へ
        return "/members/mypage/"