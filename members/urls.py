from django.urls import path
from . import views

urlpatterns = [
    path("reservations/", views.reservation_list, name="reservation_list"),
    path("favorites/", views.favorite_list, name="favorite_list"),
    path("payment/", views.payment_edit, name="payment_edit"),
    path("cancel/", views.cancel_subscription, name="cancel_subscription"),
]
