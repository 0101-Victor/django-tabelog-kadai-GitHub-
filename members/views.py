from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from members.models import Reservation, Favorite, PaymentMethod, Subscription
from members.forms import ProfileForm, PaymentForm,SubscriptionForm
from accounts.models import Profile
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

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

# 有料プラン登録
@login_required
def subscription(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # ダミー処理：実際の決済は行わない
            Subscription.objects.update_or_create(
                user=request.user,
                defaults={"is_active": True},
            )

            # 確認メール送信（ダミー）
            send_mail(
                subject="NAGOYAMESHI 有料プラン登録完了",
                message="有料プランにご登録いただきありがとうございます！",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True,
            )

            messages.success(request, "有料プランへの登録が完了しました。")
            return redirect("top")   # ← マイページではなくトップにリダイレクト
    else:
        form = SubscriptionForm()

    return render(request, "accounts/subscription.html", {"form": form})


# 有料プラン解約
@login_required
def cancel_subscription(request):
    subscription = Subscription.objects.filter(user=request.user, is_active=True).first()
    if request.method == "POST" and subscription:
        subscription.is_active = False
        subscription.save()
        messages.success(request, "有料プランを解約しました。")
        return redirect("top")

    return render(request, "pages/cancel_subscription.html")
