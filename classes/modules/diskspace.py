import os
from classes.core import Main
from classes.modules.slack import MainSlack


class MainDiskSpace(Main):
    def __getdiskfree(self):
        s = os.statvfs('/')
        d = (s.f_bavail * s.f_frsize)
        return d

    def __humanbytes(self, num):
        for x in ['bytes','KB','MB','GB']:
            if num < 1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, 'TB')

    def alertdisk(self):
        free = MainDiskSpace().__getdiskfree()
        if free >= 5368709120:
            self.value = MainDiskSpace().__humanbytes(free)
            MainSlack.slack(Main.slack_webhook_url, "Alert disk on host " + self.hostname + ", now available: "
                       + str(self.value), self.hostname, self.icon)

