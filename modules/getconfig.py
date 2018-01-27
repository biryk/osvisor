import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    slack_webhook_url = config['SLACK']['slack_webhook_url']
    admin_mail = config['DEFAULT']['admin_mail']
