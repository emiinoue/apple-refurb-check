import os
import requests

URL = "https://www.apple.com/jp/shop/refurbished/ipad/ipad-mini"
LINE_TOKEN = os.environ.get("LINE_TOKEN")
USER_ID = os.environ.get("USER_ID")

def send_line(msg):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}", "Content-Type": "application/json"}
    data = {"to": USER_ID, "messages": [{"type": "text", "text": msg}]}
    requests.post(url, headers=headers, json=data)

def check():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    try:
        r = requests.get(URL, headers=headers, timeout=15)
        # 商品リストの項目（grid-item）がページ内に存在するかチェック
        if "refurbished-category-grid-item" in r.text:
            send_line("【在庫あり】iPad miniの整備済製品が出品されました！\n" + URL)
        else:
            print("商品リストが見つかりません（在庫なし）。")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check()
