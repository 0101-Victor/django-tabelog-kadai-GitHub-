from django.db import models
from .category import Category 

class Store(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    holiday = models.CharField(max_length=50, blank=True, null=True)
    seating_capacity = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    categories = models.ManyToManyField(Category, related_name="stores", blank=True)
    image = models.ImageField(upload_to="restaurants/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name