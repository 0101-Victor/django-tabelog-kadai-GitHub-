from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models.item import Store
from base.models.review import Review
from django.views.generic import ListView
from base.models import Item # トップページにアイテム一覧を表示するために設定


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

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        Review.objects.create(
            store=store,
            reviewer_name=request.user.username,  # ログインユーザーの名前
            rating=rating,
            comment=comment,
        )
        return redirect("store_detail", store_id=store.id)

    reviews = store.reviews.all().order_by("-created_at")
    return render(request, "pages/stores_detail.html", {"store": store, "reviews": reviews})