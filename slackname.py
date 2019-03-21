#!/usr/bin/python3

from slackclient import SlackClient
import csv, time, sys

# If an API call fails, how many seconds to wait before trying again
RATE_LIMIT_SLEEP = 60

class Executor(object):
    def __init__(self, client):
        self._client = client
        self._profile = {}

    def execute(self, command):
        '''
        command is a tuple (field, value)
        if @p field is 'delay', we sleep for the provided time (and sync with slack)
        otherwise, we update an internal field. e.g.:
            display_name
            real_name
        the following might also work, but unconfirmed:
            first_name
            last_name
            image_512 (give it a URL)
            image_192 (URL)
            image_72 (URL)
            image_32 (URL)
            title
            skype
            email
            status_emoji
        '''
        field, value = command
        if field == 'delay':
            self._set_api()
            time.sleep(float(value))
        else:
            self._profile[field] = value

    def _set_api(self):
        '''
        let slack know about our desired profile info
        '''
        while True:
            resp = self._client.api_call('users.profile.set', profile=self._profile)
            if resp.get('ok'):
                break
            print(resp)
            time.sleep(RATE_LIMIT_SLEEP)

def main():
    token = open('api.token', 'r').read().strip()
    client = SlackClient(token)
    print(client.api_call('users.profile.get'))
    executor = Executor(client)

    while True:
        for command in csv.reader(open(sys.argv[1])):
            print(command)
            executor.execute(command)

if __name__ == '__main__':
    main()
