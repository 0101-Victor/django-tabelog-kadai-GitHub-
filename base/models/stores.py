# base/models/stores.py
from django.db import models
from .category import Category   # ← 追加

class Store(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    budget = models.IntegerField()
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    holiday = models.CharField(max_length=100, blank=True, null=True)
    seating_capacity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="stores")  # ★カテゴリを複数持てるように変更

    def __str__(self):
        return self.name
