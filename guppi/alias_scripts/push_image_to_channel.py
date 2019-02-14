from guppi import Guppi
import argparse
import cv2
from pathlib import Path

'''
    Script intended to be used for pushing a single image to a given slack channel with 
    a one-line ternimal command.
    
    A alias for this script is created in your .bashrc

'''

parser = argparse.ArgumentParser(
    description='Send a image with message to a slack channel. This interface use the token provided in the exported ' +
                'guppi_api_token environment variable. Currently only supports one token (i. e: one slack workspace)'
)
parser.add_argument('channel', type=str, help='The slack channel name.')
parser.add_argument('image', type=str, help='Image path')
parser.add_argument('message', type=str, help='A string encapsulated by \" \"', default='')
args = parser.parse_args()

if not Path(args.image).exists():
    raise FileNotFoundError(args.image)

image = cv2.cvtColor(cv2.imread(args.image), cv2.COLOR_BGR2RGB)
Guppi().send_image(image, args.channel, message=args.message)
