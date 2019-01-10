import os

def send_message(hook, message):

    start = 'curl -X POST -H \'Content-type: application/json\' --data \'{\"text\":\"'

    end = '\"}\' '
    cmd = f'{start}{message}{end}{hook}'

    os.system(cmd)

if __name__ == '__main__':
    hook = 'https://hooks.slack.com/services/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'
    message = 'SlackMessage'
    send_message(hook, message)