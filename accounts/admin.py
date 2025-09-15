from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile


# Profile を User の下にインライン表示する
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "プロフィール"


# UserAdmin を拡張
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    # 管理画面で表示するカラムを追加
    list_display = ("username", "email", "first_name", "last_name", "is_staff")


# 既存の UserAdmin を上書き
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Profile 単独でも編集できるように登録（不要なら削除可）
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "phone", "job")
    search_fields = ("full_name", "full_name_kana", "phone", "job")
