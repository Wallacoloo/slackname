#!/usr/bin/python3

from slackclient import SlackClient
import csv, time

# If an API call fails, how many seconds to wait before trying again
rate_limit_sleep = 60

token = open("api.token", "r").read().strip()
client = SlackClient(token)


def change_name_to(name):
    while True: # yuck
        resp = client.api_call("users.profile.set", profile=dict(display_name=name))
        if resp.get('ok'):
            break
        print(resp)
        time.sleep(rate_limit_sleep)


while True:
    for command in csv.reader(open("commands.csv")):
        delay, name = command
        delay = float(delay)
        print("name = {name} for {delay} seconds".format(**globals()))
        change_name_to(name)
        time.sleep(delay)

