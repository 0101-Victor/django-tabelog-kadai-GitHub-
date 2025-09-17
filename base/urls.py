from django.contrib import admin
from django.urls import path, include
from .views import item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),              # base アプリのURL
    path("stores/<int:store_id>/review/", item.add_review, name="add_review"),
]