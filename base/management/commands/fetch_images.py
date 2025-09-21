import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from base.models.item import Store

class Command(BaseCommand):
    help = "外部URLから画像をダウンロードして Store.image に保存"

    def handle(self, *args, **kwargs):
        stores = [
            {
                "id": 1,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main1.jpg"
            },
            {
                "id": 2,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main2.jpg"
            },
            {
                "id": 3,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main3.jpg"
            },
            {
                "id": 4,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main4.jpg"
            },
            {
                "id": 5,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main5.jpg"
            },
            {
                "id": 6,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main6.jpg"
            },
            {
                "id": 7,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main7.jpg"
            },
            {
                "id": 8,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main8.jpg"
            },
            {
                "id": 9,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main9.jpg"
            },
            {
                "id": 10,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main10.jpg"
            },
            {
                "id": 11,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main11.jpg"
            },
            {
                "id": 12,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main12.jpg"
            },
            {
                "id": 13,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main13.jpg"
            },
            {
                "id": 14,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main14.jpg"
            },
            {
                "id": 15,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main15.jpg"
            },
            {
                "id": 16,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main16.jpg"
            },
            {
                "id": 17,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main17.jpg"
            },
            {
                "id": 18,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main18.jpg"
            },
            {
                "id": 19,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main19.jpg"
            },
            {
                "id": 20,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main20.jpg"
            },
            {
                "id": 21,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main21.jpg"
            },
            {
                "id": 22,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main22.jpg"
            },
            {
                "id": 23,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main23.jpg"
            },
            {
                "id": 24,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main24.jpg"
            },
            {
                "id": 25,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main25.jpg"
            },
            {
                "id": 26,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main26.jpg"
            },
            {
                "id": 27,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main27.jpg"
            },
            {
                "id": 28,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main28.jpg"
            },
            {
                "id": 29,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main29.jpg"
            },
            {
                "id": 30,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main30.jpg"
            },
            {
                "id": 31,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main31.jpg"
            },
            {
                "id": 32,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main32.jpg"
            },
            {
                "id": 33,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main33.jpg"
            },
            {
                "id": 34,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main34.jpg"
            },
            {
                "id": 35,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main35.jpg"
            },
            {
                "id": 36,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main36.jpg"
            },
            {
                "id": 37,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main37.jpg"
            },
            {
                "id": 38,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main38.jpg"
            },
            {
                "id": 39,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main39.jpg"
            },
            {
                "id": 40,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main40.jpg"
            },
            {
                "id": 41,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main41.jpg"
            },
            {
                "id": 42,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main42.jpg"
            },
            {
                "id": 43,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main43.jpg"
            },
            {
                "id": 44,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main44.jpg"
            },
            {
                "id": 45,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main45.jpg"
            },
            {
                "id": 46,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main46.jpg"
            },
            {
                "id": 47,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main47.jpg"
            },
            {
                "id": 48,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main48.jpg"
            },
            {
                "id": 49,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main49.jpg"
            },
            {
                "id": 50,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main50.jpg"
            },
            {
                "id": 51,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main51.jpg"
            },
            {
                "id": 52,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main52.jpg"
            },
            {
                "id": 53,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main53.jpg"
            },
            {
                "id": 54,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main54.jpg"
            },
            {
                "id": 55,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main55.jpg"
            },
            {
                "id": 56,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main56.jpg"
            },
            {
                "id": 57,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main57.jpg"
            },
            {
                "id": 58,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main58.jpg"
            },
            {
                "id": 59,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main59.jpg"
            },
            {
                "id": 60,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main60.jpg"
            },
            {
                "id": 61,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main61.jpg"
            },
            {
                "id": 62,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main62.jpg"
            },
            {
                "id": 63,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main63.jpg"
            },
            {
                "id": 64,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main64.jpg"
            },
            {
                "id": 65,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main65.jpg"
            },
            {
                "id": 66,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main66.jpg"
            },
            {
                "id": 67,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main67.jpg"
            },
            {
                "id": 68,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main68.jpg"
            },
            {
                "id": 69,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main69.jpg"
            },
            {
                "id": 70,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main70.jpg"
            },
            {
                "id": 71,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main71.jpg"
            },
            {
                "id": 72,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main72.jpg"
            },
            {
                "id": 73,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main73.jpg"
            },
            {
                "id": 74,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main74.jpg"
            },
            {
                "id": 75,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main75.jpg"
            },
            {
                "id": 76,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main76.jpg"
            },
            {
                "id": 77,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main77.jpg"
            },
            {
                "id": 78,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main78.jpg"
            },
            {
                "id": 79,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main79.jpg"
            },
            {
                "id": 10,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main80.jpg"
            },
            {
                "id": 81,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main81.jpg"
            },
            {
                "id": 82,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main82.jpg"
            },
            {
                "id": 83,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main83.jpg"
            },
            {
                "id": 84,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main84.jpg"
            },
            {
                "id": 85,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main85.jpg"
            },
            {
                "id": 86,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main86.jpg"
            },
            {
                "id": 87,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main87.jpg"
            },
            {
                "id": 88,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main88.jpg"
            },
            {
                "id": 89,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main89.jpg"
            },
            {
                "id": 90,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main90.jpg"
            },
            {
                "id": 91,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main91.jpg"
            },
            {
                "id": 92,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main92.jpg"
            },
            {
                "id": 93,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main93.jpg"
            },
            {
                "id": 94,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main94.jpg"
            },
            {
                "id": 95,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main95.jpg"
            },
            {
                "id": 96,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main96.jpg"
            },
            {
                "id": 97,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main97.jpg"
            },
            {
                "id": 98,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main98.jpg"
            },
            {
                "id": 99,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main99.jpg"
            },
            {
                "id": 100,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main100.jpg"
            },
            {
                "id": 101,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main101.jpg"
            },
            {
                "id": 102,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main102.jpg"
            },
            {
                "id": 103,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main103.jpg"
            },
            {
                "id": 104,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main104.jpg"
            },
            {
                "id": 105,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main105.jpg"
            },
            {
                "id": 106,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main106.jpg"
            },
            {
                "id": 107,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main107.jpg"
            },
            {
                "id": 108,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main108.jpg"
            },
            {
                "id": 109,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main109.jpg"
            },
            {
                "id": 110,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main110.jpg"
            },
            {
                "id": 111,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main111.jpg"
            },
            {
                "id": 112,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main112.jpg"
            },
            {
                "id": 113,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main113.jpg"
            },
            {
                "id": 114,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main114.jpg"
            },
            {
                "id": 115,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main115.jpg"
            },
            {
                "id": 116,
                "url": "https://nagoyameshi-pattern-1.herokuapp.com/images/main116.jpg"
            },
        ]

        for s in stores:
            try:
                store = Store.objects.get(id=s["id"])
                response = requests.get(s["url"])
                if response.status_code == 200:
                    img_temp = NamedTemporaryFile()
                    img_temp.write(response.content)
                    img_temp.flush()
                    store.image.save(f"store_{store.id}.jpg", File(img_temp), save=True)
                    self.stdout.write(self.style.SUCCESS(f"✓ {store.name} の画像を保存しました"))
            except Store.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"× Store id={s['id']} が存在しません"))
