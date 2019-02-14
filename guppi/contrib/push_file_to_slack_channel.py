from guppi import Guppi
import sys

'''
    script intended to be used for pushing a single file to a given slack channel with 
    a one-line ternimal command.
    
    Simple usecase: 
      python -m guppi.contrib.push_file_to_slack_channel "/home/Dave/show_this.pdf" "this" "guppi" 

'''

file = sys.argv[1]
message = sys.argv[2]
channel = sys.argv[3]

Guppi().send_file(file, channel, message)