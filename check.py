import os
import requests

# iPad 整備品ページ
URL = "https://www.apple.com/jp/shop/refurbished/ipad"

# GitHubの「Secrets」から取得するように変更（後述）
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
    res = requests.post(url, headers=headers, json=data)
    print(f"LINE通知ステータス: {res.status_code}")

def check():
    # AppleのサイトはBotを弾くことがあるため、ブラウザのふりをする設定を追加
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    r = requests.get(URL, headers=headers)
    
    # 判定ポイント：
    # 現在のAppleのサイトは、在庫がない場合でもHTML内に "iPad mini" という文字が含まれていることがあります。
    # より正確には「在庫リスト」の部分をチェックする必要がありますが、まずは文字検知でテストしましょう。
    if "iPad mini" in r.text:
        send_line("Apple公式サイトに iPad mini の整備済製品が掲載されています！\n" + URL)
    else:
        print("現在は在庫がないようです。")

if __name__ == "__main__":
    check()
