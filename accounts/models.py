from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    furigana = models.CharField(max_length=150, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username