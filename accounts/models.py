from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    full_name_kana = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=50, blank=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# User が保存されたら Profile も保存
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()