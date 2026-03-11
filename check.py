import requests

# iPad 整備品ページ
URL = "https://www.apple.com/jp/shop/refurbished/ipad"

# LINEの設定
LINE_TOKEN = "LINE token goes here"  # 半角英数字だけ
USER_ID = "User ID goes here"

def send_line(msg):
    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"  # ←ここを修正
    }

    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": msg
            }
        ]
    }

    # json= を使うと自動で UTF-8 で送信されます
    requests.post(url, headers=headers, json=data)

def check():
    r = requests.get(URL)

    if "iPad mini" in r.text:
        send_line("The iPad mini has been uploaded.")  # 日本語・英語・絵文字OK

# 実行
check()
