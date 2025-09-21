# base/management/commands/assign_store_images.py
import os
import random
from django.core.management.base import BaseCommand
from base.models.item import Store

class Command(BaseCommand):
    help = "Store に sample 画像をランダムで割り当てる"

    def handle(self, *args, **kwargs):
        # sample画像があるディレクトリ
        image_dir = "media/restaurants"
        images = [f for f in os.listdir(image_dir) if f.startswith("sample") and f.endswith(".jpg")]

        if not images:
            self.stdout.write(self.style.ERROR("sample*.jpg が見つかりません"))
            return

        stores = Store.objects.all()
        for store in stores:
            filename = random.choice(images)
            store.image.name = f"restaurants/{filename}"
            store.save()
            self.stdout.write(self.style.SUCCESS(f"{store.name} → {filename}"))
