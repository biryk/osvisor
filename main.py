from modules.slack import Mods
from modules.diskspace import alertdisk
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
slack_webhook_url = config['SLACK']['slack_webhook_url']
hostname = ['DEFAULT']['hostname']
icon = ['DEFAULT']['icon']
admin_mail = config['DEFAULT']['admin_mail']


def main():
    if alertdisk() == 1:
        Mods.slack(slack_webhook_url, "Alert disk on host", hostname, icon)
    else:
        pass


if __name__ == "__main__":
        main()

