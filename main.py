import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    slack_webhook_url = config['SLACK']['slack_webhook_url']
    admin_mail = config['DEFAULT']['admin_mail']
    print(admin_mail)


if __name__ == "__main__":
        main()
