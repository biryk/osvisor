import requests
import json
from classes.core import Main


class Mods(Main):
    @classmethod
    def slack(cls, hook_url, message, host, emoji):
        data = {
            'text': message,
            'username': host,
            'icon_emoji': emoji
            }
        requests.post(hook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
