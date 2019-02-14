from guppi import Guppi
import argparse
from pathlib import Path

'''
    Script intended to be used for pushing a single file to a given slack channel with 
    a one-line ternimal command.

    A alias for this script is created in your .bashrc

'''

parser = argparse.ArgumentParser(
    description='Send a file with a message to a slack channel. This interface use the token provided in the exported ' +
                'guppi_api_token environment variable. Currently only supports one token (i. e: one slack workspace)'
)
parser.add_argument('channel', type=str, help='The slack channel name.')
parser.add_argument('file', type=str, help='file path')
parser.add_argument('message', type=str, help='A string encapsulated by \" \"', default='')
args = parser.parse_args()

if not Path(args.file).exists():
    raise FileNotFoundError(args.file)

Guppi().send_file(args.file, args.channel, message=args.message)