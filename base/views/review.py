from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from base.models.review import Review

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # 自分のレビュー or 管理者 以外は削除禁止
    if review.user != request.user and not request.user.is_staff:
        raise PermissionDenied("このレビューを削除する権限がありません")

    review.delete()
    messages.success(request, "レビューを削除しました。")
    return redirect("store_detail", store_id=review.store.id)
