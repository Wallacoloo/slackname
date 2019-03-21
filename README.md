This application animates a Slack user's display name. Due to stupid, stupid
rate limiting, it's limited to an effective 0.1 frames per second or so, but
animations can be made that have higher burst rates. The rate-limiting details
are intentionally left undocumented by Slack because not documenting your public
interfaces is all the new rage! (actually, this has been the confusing standard
in many industries since time immemorial. Why on _earth_ should a processor's
documentation be confidential?)

# Setup

```
pacaur -S python-slackclient
```

Or:

```
python3 -m pip install --user slackclient
```

Navigate to https://api.slack.com/custom-integrations/legacy-tokens and obtain an API token.
Save that token to a file named "api.token".
Run `./slackname.py <path/to/commands.csv>`
