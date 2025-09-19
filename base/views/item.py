from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models.item import Store
from django.contrib import messages
from base.models.review import Review
from django.views.generic import ListView
from base.models import Item # トップページにアイテム一覧を表示するために設定
from members.models import Subscription

class IndexListView(ListView):
    model = Item # djangoがアイテムモデルの一覧からデータをもってきてくれる設定
    template_name = 'pages/index.html' # どのテンプレとを返していくのかを記載

def index(request):
    object_list = Item.object.all()
    context = {
        'object_list': object_list,
    }
    return render(request, 'pages/index.html', context)

@login_required
def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    reviews = store.reviews.all().order_by("-created_at")

    # 有料プランかどうか確認
    is_premium = Subscription.objects.filter(user=request.user, is_active=True).exists()

    if request.method == "POST":
        if not is_premium:
            messages.error(request, "有料会員のみレビュー投稿ができます。")
            return redirect("subscription")

        review_id = request.POST.get("review_id")
        if review_id:  # 編集
            review = get_object_or_404(Review, id=review_id, user=request.user)
            review.rating = request.POST["rating"]
            review.comment = request.POST["comment"]
            review.save()
            messages.success(request, "レビューを更新しました！")
        else:  # 新規投稿
            Review.objects.create(
                store=store,
                user=request.user,
                reviewer_name=request.user.username,
                rating=request.POST["rating"],
                comment=request.POST["comment"],
            )
            messages.success(request, "レビューを投稿しました！")
        return redirect("store_detail", store_id=store.id)

    return render(request, "pages/stores_detail.html", {
        "store": store,
        "reviews": reviews,
        "is_premium": is_premium,
    })