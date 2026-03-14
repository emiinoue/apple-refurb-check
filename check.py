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
        html_text = r.text

        # 判定用ワード（これらが含まれていたら「在庫なし」）
        no_stock_keywords = ["在庫がありません", "しばらくしてからもう一度", "お近くの店舗"]
        
        is_no_stock = any(k in html_text for k in no_stock_keywords)

        if is_no_stock:
            print("在庫なしを確認。")
        else:
            # 原因調査のため、ページ冒頭のテキストを添えて通知
            debug_text = html_text[:200].replace('\n', ' ')
            send_line(f"【判定中】変化あり？\n確認用テキスト: {debug_text}\n{URL}")
            
    except Exception as e:
        send_line(f"エラー発生: {e}")

if __name__ == "__main__":
    check()
