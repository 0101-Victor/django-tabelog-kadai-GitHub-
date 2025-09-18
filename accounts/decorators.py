from django.shortcuts import redirect
from django.contrib import messages
from members.models import Subscription
from accounts.decorators import paid_member_required

def paid_member_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "レビューを投稿するにはログインしてください。")
            return redirect("login")

        # 有料プラン加入チェック
        if not Subscription.objects.filter(user=request.user, is_active=True).exists():
            messages.error(request, "有料会員のみレビューを投稿・編集・削除できます。")
            return redirect("subscription")  # 有料プラン登録ページへ誘導
        return view_func(request, *args, **kwargs)
    return _wrapped_view
