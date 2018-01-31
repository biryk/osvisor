from classes.modules.slack import MainSlack
from classes.modules.diskspace import MainDiskSpace as aler
from classes.modules.checkhosts import MainRequest
from classes.core import Main


def main():
    if aler().alertdisk() != 0:
        MainSlack.slack(Main.slack_webhook_url, "Alert disk on host " + Main.hostname +
                        ", now available: " + str(aler().alertdisk()), Main.hostname, Main.icon)
    else:
        pass
    MainRequest().sort_host()


if __name__ == "__main__":
    main()


