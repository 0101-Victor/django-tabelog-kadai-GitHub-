from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Reservation, Review, Favorite, Restaurant

# admin.site.register(Category)
# admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Favorite)


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    resource_class = RestaurantResource
