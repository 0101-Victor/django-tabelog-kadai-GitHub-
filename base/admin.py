from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models.item import Store
from .models.review import Review
from .models.category import Category

class ReviewResource(resources.ModelResource):
    store = fields.Field(
        column_name="store_id",
        attribute="store",
        widget=ForeignKeyWidget(Store, "id")
    )

    class Meta:
        model = Review
        fields = ("id", "store", "reviewer_name", "rating", "comment", "created_at")
        import_id_fields = ("id",)


# Store 編集画面で Review をインライン表示
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

@admin.register(Store)
class StoreAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "budget", "postal_code", "address", "opening_hours", "holiday", "seating_capacity")
    search_fields = ("name", "address")
    inlines = [ReviewInline]
    filter_horizontal = ("categories",)  # 管理画面でカテゴリを複数選択できるようにする

# Review 管理画面（インポート/エクスポート用）
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource
    list_display = ("id", "store", "reviewer_name", "rating", "created_at")
    search_fields = ("store__name", "reviewer_name", "comment")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)