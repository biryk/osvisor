import requests
import socket
from classes.core import Main
from classes.modules.slack import MainSlack


class MainRequest(Main):

    def checkurl(self, url):
        try:
            req = requests.get(url).status_code
        except:
            pass
            req = 'error connect'
        return req

    def checkport(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2.0)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return 0
        else:
            return 1

    def sort_host(self):
        file_hosts = open('hosts.txt', 'r')
        for line in file_hosts:
            ip_splited = line.split(',')
            ip = ip_splited[0]
            port = int(ip_splited[1])
            try:
                r = self.checkport(ip, port)
            except socket.gaierror:
                return print("invalid config")
            if r == 1:
                MainSlack.slack(Main.slack_webhook_url, "Host not available: " + str(ip) + " port: " + str(port), Main.hostname, Main.icon)
            else:
                pass



