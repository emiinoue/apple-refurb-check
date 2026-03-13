import os
import requests

# iPad 整備品ページ
URL = "https://www.apple.com/jp/shop/refurbished/ipad"

# 金庫（Secrets）から合鍵を取り出す設定
LINE_TOKEN = os.environ.get("LINE_TOKEN")
USER_ID = os.environ.get("USER_ID")

def send_line(msg):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": msg}]
    }
    # LINEに送信
    res = requests.post(url, headers=headers, json=data)
    print(f"LINE通知ステータス: {res.status_code}")

def check():
    # AppleのBot対策を突破するための設定
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        r = requests.get(URL, headers=headers, timeout=15)
        # ここを「iPad mini」に戻しました！
        if "iPad mini" in r.text:
            send_line("Apple公式サイトに iPad mini の整備済製品が掲載されています！\n" + URL)
        else:
            print("現在は在庫がないようです。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    check()
