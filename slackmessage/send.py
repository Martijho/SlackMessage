import os

def send_message(hook, message):

    start = 'curl -X POST -H \'Content-type: application/json\' --data \'{\"text\":\"'

    end = '\"}\' '
    cmd = f'{start}{message}{end}{hook}'

    os.system(cmd)
