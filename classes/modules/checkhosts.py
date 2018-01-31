import requests
import socket
from classes.core import Main
from classes.modules.slack import MainSlack


class MainRequest(Main):

    def checkurl(self, url):
        req = requests.get(url).status_code
        return req

    def checkport(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2.0)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return 0
        else:
            return 1

    def check_file_hosts(self):
        try:
            file_hosts = open('config/hosts.conf', 'r')
        except FileNotFoundError:
            return

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

    def check_file_urls(self):
        try:
            file_urls = open('config/urls.conf', 'r')
        except FileNotFoundError:
            return

        for line in file_urls:
            try:
                url_code = self.checkurl(line.rstrip('\n'))
            except:
                 print('check error: ' + line)
                 url_code = 'url error'
                 pass
            try:
                if url_code != 200:
                    MainSlack.slack(Main.slack_webhook_url, "Url  not available, status code: " + str(url_code)+ ', '
                                    + line, Main.hostname, Main.icon)
                else:
                    pass
            except UnboundLocalError:
                pass



