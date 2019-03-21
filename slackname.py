#!/usr/bin/python3

from slackclient import SlackClient
import csv, time, sys

# If an API call fails, how many seconds to wait before trying again
rate_limit_sleep = 60

token = open("api.token", "r").read().strip()
client = SlackClient(token)

def change_name_to(name):
    while True: # yuck
        # some fields:
        # display_name
        # real_name
        # first_name
        # last_name
        # image_512 (give it a URL)
        # image_192 (URL)
        # image_72 (URL)
        # image_32 (URL)
        # title
        # skype
        # email
        # status_emoji
        resp = client.api_call("users.profile.set", profile=dict(real_name=name))
        if resp.get('ok'):
            break
        print(resp)
        time.sleep(rate_limit_sleep)

print(client.api_call('users.profile.get'))

while True:
    for command in csv.reader(open(sys.argv[1])):
        delay, name = command
        delay = float(delay)
        print("name = {name} for {delay} seconds".format(**globals()))
        change_name_to(name)
        time.sleep(delay)

