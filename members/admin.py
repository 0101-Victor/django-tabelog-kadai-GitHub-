from django.contrib import admin
from .models import Favorite, PaymentMethod, Reservation, Subscription


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "store_name", "date", "time", "people")
    list_filter = ("date", "time")
    search_fields = ("store_name", "user__username")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "store_name")
    search_fields = ("store_name", "user__username")


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("user", "card_type", "card_name", "card_number", "expiration_date")
    search_fields = ("card_name", "card_number", "user__username")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "plan", "start_date", "is_active")
    list_filter = ("is_active", "start_date")
    search_fields = ("user__username", "plan")
