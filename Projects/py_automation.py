import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '7122237578',
        'message': 'Hi Madisen, do you know who this is',
        'key': 'd05682f21cf12a2537d0bd32998da214a0d74568GZl9OzYU4SvJ22OH14ZAv1Y0G',
        # 'key': "textbelt",
    })
    print(resp.json())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
# schedule.every().day.at("6:00").do(send_message)

# Use textbelt.com to send automated message