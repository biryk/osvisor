import requests


def checkhost(url):
    try:
        req = requests.get(url).status_code
    except:
        pass
        req = 'error connect'
    return req
