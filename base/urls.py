from django.contrib import admin
from django.urls import path, include
from base.views import review
from .views import item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),              # base アプリのURL
    path("stores/<int:store_id>/review/", item.add_review, name="add_review"),
    path("reviews/<int:review_id>/delete/", review.delete_review, name="delete_review"),

]