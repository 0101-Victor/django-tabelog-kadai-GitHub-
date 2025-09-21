from django.contrib import admin
from django.urls import path
from base.views import review,item
from . import views
from members import views as members_views
from base.views.item import store_top, store_reserve, store_reviews, stores_by_category


urlpatterns = [
    path('', item.index, name="top"),              # base アプリのURL
    path("store/<int:store_id>/", item.store_top, name="store_top"),   # トップ
    path("store/<int:store_id>/reserve/", item.store_reserve, name="store_reserve"),  # 予約
    path("store/<int:store_id>/reviews/", item.store_reviews, name="store_reviews"),  # レビュー
    path("category/<int:category_id>/", item.stores_by_category, name="stores_by_category"),
    path("reviews/<int:review_id>/delete/", review.delete_review, name="delete_review"),
    path("subscription/", members_views.subscription, name="subscription"),
    path("cancel_subscription/", members_views.cancel_subscription, name="cancel_subscription"),
]