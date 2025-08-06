import time
import random
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/__Webhook ID__/__Webhook Token__"

quotes = [
    "Jesus Christ says you should download [my software](https://github.com/Epicinver)",
    "Let there be [Python](https://python.org), let there be [Visual Basic](https://visualstudio.com), let there be EVERYTHING",
    "uwu",
    "He said: push to main, and [GitHub](https://github.com/) approved.",
    "Made by Epicinver on GitHub, please support me <3"
]

def send_quote():
    embed = {
        "embeds": [
            {
                "title": "Quote of the day:",
                "description": random.choice(quotes),
                "color": 0xD41D81,
                "footer": {"text": "the holy quote sender - 69/69/6969, 69:69"}
            }
        ]
    }

    response = requests.post(WEBHOOK_URL, json=embed)
    if response.status_code == 204:
        print("✨ Quote sent!")
    else:
        print(f"⚠ Failed to send: {response.status_code} - {response.text}")

while True:
    send_quote()
    time.sleep(500)  # 8 minutes

# Change the WebhookURL, and change the quotes if you want to.
