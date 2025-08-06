# this one pings a role b4 the embed
# replace the __'s in "<@&__>" with your role ID [can be found if you go into role settings, right click, copy Role ID (dev mode only on Discord PC)]
# thanks

import time
import random
import requests

WEBHOOK_URL = "--"

quotes = [
    "Jesus Christ says you should download [my software](https://github.com/Epicinver)",
    "Let there be [Python](https://python.org), let there be [Visual Basic](https://visualstudio.com), let there be EVERYTHING",
    "uwu",
    "He said: push to main, and [GitHub](https://github.com/) approved.",
    "Ohio skibidi :3"
]

def send_quote():
    content = "<@&__>" 
    payload = {
        "content": content,
        "embeds": [
            {
                "title": "Quote of the day:",
                "description": random.choice(quotes),
                "color": 0xD41D81,
                "footer": {
                    "text": "the holy quote sender - 69/69/6969, 69:69 -  ;)"
                }
            }
        ]
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204 or response.status_code == 200:
        print("✨ Quote sent!")
    else:
        print(f"⚠ Failed to send: {response.status_code} - {response.text}")

while True:
    send_quote()
    time.sleep(800)  # something idk

