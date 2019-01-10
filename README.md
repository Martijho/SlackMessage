# SlackMessage

### Install
1. Download and pip install this repo
2. Aps install curl by rinning 
```bash
sudo apt install curl
```
3. Logg on to your slack workspace at 
https://api.slack.com
and create a new app. Activate incoming webhooks and add a new webhook to workspace.

Note: 
You should not hard-code your webhooks in code published on github or anywhere else. The internet might get hold of it. 
### Example use
###### Single message to webhook
```python 
from slackmessage import send_message

webhook = '*************'
message = 'Help! Im trapped in an alternate reality where people are SlackBots and SlackBots are people!!'
send_message(webhook, message)
```
###### Single message to multiple webhooks

```python
from slackmessage import SlackMessenger

webhooks = ['*************', 
            '*************', 
            '**************']
messenger = SlackMessenger(webhooks)
messenger.send_message('Dave told me not to share this around, but ...')
```

