from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models.item import Store
from .models.review import Review

# Store画面からレビューを直接追加できるようにする
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # 新規入力欄を1つ余分に表示

# Store用の管理クラス
@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "budget", "postal_code", "address","opening_hours", "holiday", "seating_capacity", "category",)
    search_fields = ("id", "name", "description", "budget", "postal_code", "address","opening_hours", "holiday", "seating_capacity", "category",)
    inlines = [ReviewInline]

# Review を独立して管理画面にも出す（インポート/エクスポート用）
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ("store", "reviewer_name", "rating", "comment", "created_at")
    search_fields = ("store__name", "reviewer_name", "comment")