from django.contrib import admin
from .models.item import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "budget", "description", "address", "created_at")
    search_fields = ("name", "category", "budget", "description", "address", "created_at")
admin.site.register(Store, StoreAdmin)