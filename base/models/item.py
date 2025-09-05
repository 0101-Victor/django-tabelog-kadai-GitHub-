# base/models/item.py
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name