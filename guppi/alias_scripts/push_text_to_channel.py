from guppi import Guppi
import argparse

'''
    Script intended to be used for pushing a single message to a given slack channel with 
    a one-line ternimal command.
    
    A alias for this script is created in your .bashrc
    
'''

parser = argparse.ArgumentParser(
    description='Send a string to a slack channel. This interface use the token provided in the exported ' +
                'guppi_api_token environment variable. Currently only supports one token (i. e: one slack workspace)'
)
parser.add_argument('channel', type=str, help='The slack channel name.')
parser.add_argument('message', type=str, help='A string encapsulated by \" \"')
args = parser.parse_args()

Guppi().send(args.message, args.channel)