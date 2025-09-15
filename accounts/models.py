from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    full_name_kana = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username