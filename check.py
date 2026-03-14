import os
import requests

URL = "https://www.apple.com/jp/shop/refurbished/ipad/ipad-mini" # mini専用ページに変更
LINE_TOKEN = os.environ.get("LINE_TOKEN")
USER_ID = os.environ.get("USER_ID")

def send_line(msg):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}", "Content-Type": "application/json"}
    data = {"to": USER_ID, "messages": [{"type": "text", "text": msg}]}
    requests.post(url, headers=headers, json=data)

def check():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(URL, headers=headers, timeout=15)
        # 「在庫なし」の時に出る特定の文章が含まれて「いない」ことを確認する
        if "現在、在庫がありません" in r.text or "在庫がありません" in r.text:
            print("在庫なしを確認。")
        else:
            # ページ構成が変わったり、商品が出現したりした場合に通知
            send_line("【速報】iPad miniの在庫が更新された可能性があります！\n" + URL)
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    check()
