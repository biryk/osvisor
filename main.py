#!/usr/bin/python3.5

from classes.modules.diskspace import MainDiskSpace
from classes.modules.checkhosts import MainRequest


def main():
    MainDiskSpace().alertdisk()
    MainRequest().check_file_hosts()
    MainRequest().check_file_urls()

if __name__ == "__main__":
    main()


