from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from base.models.item import Store
from base.models.review import Review
from base.models.category import Category
from members.models import Subscription
from members.models import Reservation

def index(request):
    stores = Store.objects.all()
    top_rated_stores = (
        Store.objects.annotate(avg_rating=Avg("reviews__rating"))
        .order_by("-avg_rating")[:6]
    )
    categories = Category.objects.all()
    return render(request, "pages/index.html", {
        "stores": stores,
        "top_rated_stores": top_rated_stores,
        "categories": categories,
    })


def store_top(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    is_premium = request.user.is_authenticated and Subscription.objects.filter(user=request.user, is_active=True).exists()
    return render(request, "pages/store_top.html", {"store": store, "is_premium": is_premium})

@login_required
def store_reserve(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    is_premium = request.user.is_authenticated and Subscription.objects.filter(
        user=request.user, is_active=True
    ).exists()

    # 有料会員チェック
    if not is_premium:
        messages.error(request, "予約は有料会員限定です。")
        return redirect("subscription")

    if request.method == "POST":
        Reservation.objects.create(
            user=request.user,
            store=store,
            reservation_date=request.POST["reservation_date"],
            reservation_time=request.POST["reservation_time"],
            number_of_people=request.POST["number_of_people"],
        )
        messages.success(request, "予約が完了しました！")
        return redirect("mypage")

    return render(
        request,
        "pages/store_reserve.html",
        {"store": store, "is_premium": is_premium},
    )

def store_reviews(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    reviews = store.reviews.all().order_by("-created_at")
    is_premium = request.user.is_authenticated and Subscription.objects.filter(
        user=request.user, is_active=True
    ).exists()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "レビュー投稿にはログインが必要です。")
            return redirect("login")
        if not is_premium:
            messages.error(request, "有料会員のみレビュー投稿・編集・削除ができます。")
            return redirect("subscription")

        review_id = request.POST.get("review_id")
        if review_id:
            review = get_object_or_404(Review, id=review_id, user=request.user)
            review.rating = request.POST["rating"]
            review.comment = request.POST["comment"]
            review.save()
            messages.success(request, "レビューを更新しました！")
        else:
            Review.objects.create(
                store=store,
                user=request.user,
                reviewer_name=request.user.username,
                rating=request.POST["rating"],
                comment=request.POST["comment"],
            )
            messages.success(request, "レビューを投稿しました！")
        return redirect("store_reviews", store_id=store.id)

    return render(
        request,
        "pages/store_reviews.html",
        {"store": store, "reviews": reviews, "is_premium": is_premium},
    )

def stores_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    stores = Store.objects.filter(categories=category)
    return render(request, "pages/stores.html", {
        "category": category,
        "stores": stores,
    })

def index(request):
    stores = Store.objects.all()
    top_rated_stores = (
        Store.objects.annotate(avg_rating=Avg("reviews__rating"))
        .order_by("-avg_rating")[:6]
    )
    categories = Category.objects.all()
    new_stores = Store.objects.order_by("-id")[:3]  # ← 新規掲載店、最新3件

    return render(request, "pages/index.html", {
        "stores": stores,
        "top_rated_stores": top_rated_stores,
        "categories": categories,
        "new_stores": new_stores,
    })