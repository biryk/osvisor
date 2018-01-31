import os
from classes.core import Main


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
        if free <= 5368709120:
            value = MainDiskSpace().__humanbytes(free)
            return value
        else:
            return 0
