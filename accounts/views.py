from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ログインさせたいなら次の行を有効化
            # login(request, user)

            # メッセージを出してトップへ
            messages.success(
                request,
                "登録されたメールアドレス宛にメールを送信しました。メールアドレスの認証をお願いいたします。",
            )
            return redirect("top")
    else:
        form = CustomUserCreationForm()
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