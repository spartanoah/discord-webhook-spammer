import requests
import random
import time

# Define the webhook URL
WEBHOOK_URL = 'url here'

# List of random names
names = ['join for nukies', 'discord nuke software here', 'join plz', 'join for cheap nukies', 'ez nukes', 'l bro got nuked', 'get nuked :)']

# Define the throttle interval in seconds
throttle_interval = 0.25  # Change this value to your desired throttle interval

def send_discord_message(webhook_url, name):
    payload = {
        'username': name,
        'content': 'https://discord.gg/DxVXbRXG'
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print(f'Message sent as {name}')
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    while True:
        random_name = random.choice(names)
        send_discord_message(WEBHOOK_URL, random_name)
        time.sleep(throttle_interval)
