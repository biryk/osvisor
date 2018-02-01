import os
from classes.core import Main
from classes.modules.slack import MainSlack


class MainDiskSpace(Main):
    def __getdiskfree(self, path):
        s = os.statvfs(path)
        d = (s.f_bavail * s.f_frsize)
        return d

    def __humanbytes(self, num):
        for x in ['bytes','KB','MB','GB']:
            if num < 1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, 'TB')

    def alertdisk(self):
        free_root = MainDiskSpace().__getdiskfree('/')
        if free_root <= 10737418240:
            self.value = MainDiskSpace().__humanbytes(free_root)
            MainSlack.slack(Main.slack_webhook_url, "Alert disk on host / " + self.hostname + ", now available: "
                       + str(self.value), self.hostname, self.icon)

        free_data = MainDiskSpace().__getdiskfree('/data')
        if free_data <= 10737418240:
            self.value = MainDiskSpace().__humanbytes(free_data)
            MainSlack.slack(Main.slack_webhook_url, "Alert disk on host /data " + self.hostname + ", now available: "
                       + str(self.value), self.hostname, self.icon)
        free_data2 = MainDiskSpace().__getdiskfree('/data2')
        if free_data2 <= 10737418240:
            self.value = MainDiskSpace().__humanbytes(free_data2)
            MainSlack.slack(Main.slack_webhook_url, "Alert disk /data2 on host " + self.hostname + ", now available: "
                       + str(self.value), self.hostname, self.icon)