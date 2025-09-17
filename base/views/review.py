from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from base.models.review import Review

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user and not request.user.is_staff:
        raise PermissionDenied("このレビューを編集する権限がありません")
    # フォーム処理 …（省略）

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user and not request.user.is_staff:
        raise PermissionDenied("このレビューを削除する権限がありません")
    review.delete()
    return redirect("store_detail", store_id=review.store.id)
