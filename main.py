from classes.modules.slack import Mods
from classes.modules.diskspace import alertdisk
from classes.core import Main


def main():
    if alertdisk() != 0:
        Mods.slack(Main.slack_webhook_url, "Alert disk on host " + Main.hostname + \
                   ", now available: " + str(alertdisk()), Main.hostname, Main.icon)
    else:
        pass


if __name__ == "__main__":
    main()


