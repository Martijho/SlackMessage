import os

class SlackMessenger:
    def __init__(self, hooks):
        self._hooks = hooks if type(hooks) == list else [hooks]

    def send_message(self, message):
        start = 'curl -X POST -H \'Content-type: application/json\' --data \'{\"text\":\"'
        end = '\"}\' '

        for hook in self._hooks:
            cmd = f'{start}{message}{end}{hook}'
        os.system(cmd)