from modules.slack import Mods
import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    slack_webhook_url = config['SLACK']['slack_webhook_url']
    Mods.slack(slack_webhook_url, "kukuku", "tv1", ":one:")


if __name__ == "__main__":
        main()
