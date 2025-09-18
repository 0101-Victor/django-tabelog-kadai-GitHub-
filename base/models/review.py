from django.db import models
from django.contrib.auth.models import User
from .item import Store

class Review(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)   # レビュー者名
    rating = models.FloatField()                       # ★の数（例: 4.5）
    comment = models.TextField(blank=True, null=True)  # コメント
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.store.name} - {self.reviewer_name} ({self.rating})"
