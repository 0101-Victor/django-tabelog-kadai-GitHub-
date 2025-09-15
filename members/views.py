from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from members.models import Reservation, Favorite, PaymentMethod, Subscription
from members.forms import ProfileForm, PaymentForm
from accounts.models import Profile

@login_required
def mypage(request):
    return render(request, "members/mypage.html")

# プロフィール編集
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
    return render(request, "members/profile_edit.html", {"form": form})

# 予約一覧
@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "members/reservations.html", {"reservations": reservations})

# お気に入り一覧
@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "members/favorites.html", {"favorites": favorites})

# 支払い方法編集
@login_required
def payment_edit(request):
    payment, created = PaymentMethod.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("mypage")
    else:
        form = PaymentForm(instance=payment)
    return render(request, "members/payment_edit.html", {"form": form})

@login_required
def subscription_view(request):
    # すでに有料プランに登録している場合はマイページへ
    if Subscription.objects.filter(user=request.user, is_active=True).exists():
        return redirect("mypage")

    return render(request, "members/subscription.html")

# 有料プラン解約
@login_required
def cancel_subscription(request):
    subscription, created = Subscription.objects.get_or_create(user=request.user)
    subscription.active = False
    subscription.save()
    return redirect("mypage")
