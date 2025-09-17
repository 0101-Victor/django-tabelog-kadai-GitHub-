from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models.item import Store
from .models.review import Review


# Review 用のインポート / エクスポート設定
class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
        fields = ("id", "store__name", "reviewer_name", "rating", "comment", "created_at")
        import_id_fields = ("id",)


# Store 編集画面で Review をインライン表示
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


# Store 管理画面
@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    list_display = (
        "id", "name", "description", "budget", "postal_code",
        "address", "opening_hours", "holiday", "seating_capacity", "category",
    )
    search_fields = (
        "id", "name", "description", "budget", "postal_code",
        "address", "opening_hours", "holiday", "seating_capacity", "category",
    )
    inlines = [ReviewInline]   # ← これでインライン編集もできる


# Review 管理画面（インポート/エクスポート用）
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource
    list_display = ("id", "store", "reviewer_name", "rating", "created_at")
    search_fields = ("store__name", "reviewer_name", "comment")
