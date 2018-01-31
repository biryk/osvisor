# osvisor
Need to create config/config.ini:

```conf
    [SLACK]

    slack_webhook_url = https://hook.com

    hostname = anyhost

    icon = :one: # from emoji list
```
for check for open ip:port create file config/hosts.conf

```conf
192.168.1.1, 80
192.168.1.1, 3306
```
if not open = alert

for check for 200 status code url create file config/urls.conf

```conf
https://yandex.ru
```
if code not 200 = alert

If free disk space < 5 GB , alert

