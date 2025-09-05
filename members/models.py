from django.db import models
from django.contrib.auth.models import User

# 予約
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.TimeField()
    people = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.store_name}"


# お気に入り
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.store_name}"


# 支払い方法
class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=50)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()  # MM/YY形式
    security_code = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.user.username} - {self.card_number[-4:]}"


# 有料プラン
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
