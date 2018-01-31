#!/bin/bash/python3.5
import configparser


class Main:
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    slack_webhook_url = config['SLACK']['slack_webhook_url']
    hostname = config['SLACK']['hostname']
    icon = config['SLACK']['icon']

