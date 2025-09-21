import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from base.models.item import Store
from django.conf import settings

class Command(BaseCommand):
    help = "全店舗にランダムなサンプル画像を設定する"

    def handle(self, *args, **kwargs):
        # サンプル画像のリスト
        sample_dir = os.path.join(settings.BASE_DIR, "media/restaurants")
        sample_files = ["sample1.jpg", "sample2.jpg", "sample3.jpg"]

        # 存在チェック
        valid_files = [os.path.join(sample_dir, f) for f in sample_files if os.path.exists(os.path.join(sample_dir, f))]
        if not valid_files:
            self.stdout.write(self.style.ERROR(f"× サンプル画像が見つかりません: {sample_dir}"))
            return

        # 店舗にランダムで設定
        for store in Store.objects.all():
            if not store.image:  # 画像が未設定の店舗だけ処理
                sample_path = random.choice(valid_files)
                with open(sample_path, "rb") as f:
                    store.image.save(os.path.basename(sample_path), File(f), save=True)
                self.stdout.write(self.style.SUCCESS(f"✓ {store.name} に {os.path.basename(sample_path)} を設定しました"))
            else:
                self.stdout.write(self.style.WARNING(f"△ {store.name} はすでに画像あり"))
