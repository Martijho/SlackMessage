from slackclient import SlackClient
import cv2

import os
import warnings


class Guppi:
    def __init__(self, debug=False):

        self._client = SlackClient(token=os.environ['guppi_api_token'])
                                   # client_id=os.environ['guppi_client_id'],
                                   # client_secret=os.environ['guppi_client_secret'])

        self.channels = [c for c in self._client.api_call("channels.list", exclude_archived=1)['channels']]

        self.users = {usr['name']: usr['id'] for usr in self._client.api_call('users.list')['members']}

        self.debug = debug

    def send(self, message, channel):
        '''
        Send a string to slack channel
        :param message: Sting to be sent
        :param channel: Slack channel name
        '''
        resp = self._client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )
        if not resp['ok']:
            warn_message = 'Message not sent: {}'.format(resp['error'])
            warn_message += f'\n{resp}' if self.debug else ''
            warnings.warn(warn_message)

    def send_image(self, image, channel, message=''):
        '''
        Send image (array) to channel
        :param image: image
        :param channel: channel name
        :param message: message to preced image
        '''
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_string = cv2.imencode('.jpg', image)[1].tostring()

        resp = self._client.api_call(
            'files.upload',
            channels=channel,
            filename='pic.jpg',
            file=image_string,
            initial_comment=message
        )
        if not resp['ok']:
            warn_message = 'Image not sent: {}'.format(resp['error'])
            warn_message += f'\n{resp}' if self.debug else ''
            warnings.warn(warn_message)

    def send_file(self, file_path, channel, message=''):
        '''
        Send a file to a channel
        :param file_path: path to file
        :param channel: channel name
        :param message: message to preced file
        '''
        resp =self._client.api_call(
            'files.upload',
            channels=channel,
            filename='pic.jpg',
            file=open(file_path, 'rb'),
            initial_comment=message

        )
        if not resp['ok']:
            warn_message = 'Image not sent: {}'.format(resp['error'])
            warn_message += f'\n{resp}' if self.debug else ''
            warnings.warn(warn_message)


if __name__ == '__main__':
    g = Guppi()
    g.send('TEST', 'guppi')