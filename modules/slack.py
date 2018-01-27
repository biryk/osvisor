import requests
import json


def slack(hook_url, message, host, emoji):

    data = {
        'text': message,
        'username': host,
        'icon_emoji': emoji
    }

    response = requests.post(hook_url, data=json.dumps(
        data), headers={'Content-Type': 'application/json'})

    return response.status_code
