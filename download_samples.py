import requests
import os

# ダウンロードしたい画像のURLを正しく並べる（カンマで区切る）
urls = [
    "https://nagoyameshi-pattern-1.herokuapp.com/storage/restaurants/yakitori01.jpg",
    "https://nagoyameshi-pattern-1.herokuapp.com/storage/restaurants/sakana.jpg",
    "https://nagoyameshi-pattern-1.herokuapp.com/storage/restaurants/yakiniku02.jpg",
    "https://nagoyameshi-pattern-1.herokuapp.com/storage/restaurants/oden.jpg",
    "https://nagoyameshi-pattern-1.herokuapp.com/storage/restaurants/ramen02.jpg",
]

save_dir = "media/restaurants"
os.makedirs(save_dir, exist_ok=True)

for i, url in enumerate(urls, start=1):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(save_dir, f"sample{i}.jpg")
            with open(path, "wb") as f:
                f.write(response.content)
            print(f"✓ {path} を保存しました")
        else:
            print(f"× ダウンロード失敗: {url} (status {response.status_code})")
    except Exception as e:
        print(f"⚠ エラー: {url} - {e}")
