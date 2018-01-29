import requests
import json


class Mods:
    @staticmethod
    def slack(hook_url, message, host, emoji):
        data = {
            'text': message,
            'username': host,
            'icon_emoji': emoji
            }
        requests.post(hook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
