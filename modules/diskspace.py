import os


def getdiskfree():
    s = os.statvfs('/')
    d = (s.f_bavail * s.f_frsize)
    return d


def humanbytes(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def alertdisk():
    free = getdiskfree()
    if free >= 5368709120:
        value = humanbytes(free)
        return value
    else:
        return 0
