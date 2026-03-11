import requests

URL = "https://www.apple.com/jp/shop/refurbished/ipad"

LINE_TOKEN = "ここにLINEトークン"
USER_ID = "ここにUserID"

def send_line(msg):

    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "to": USER_ID,
        "messages":[
            {
                "type":"text",
                "text": msg
            }
        ]
    }

    requests.post(url, headers=headers, json=data)


def check():

    r = requests.get(URL)

    if "iPad mini" in r.text:
        send_line("iPad mini 整備品が出ました！")


check()
