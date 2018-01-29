from modules.slack import Mods
from modules.diskspace import alertdisk
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
slack_webhook_url = config['SLACK']['slack_webhook_url']
admin_mail = config['DEFAULT']['admin_mail']
hostname = config['SLACK']['hostname']
icon = config['SLACK']['icon']


def main():
    if alertdisk() != 0:
        Mods.slack(slack_webhook_url, "Alert disk on host " + hostname + ", now available: " + str(alertdisk()), hostname, icon)
    else:
        pass


if __name__ == "__main__":
        main()
