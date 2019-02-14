from guppi import Guppi
import sys

'''
    script intended to be used for pushing a single string to a given slack channel with 
    a one-line ternimal command.
    
    Simple usecase: 
      python -m guppi.contrib.push_string_to_slack_channel "DarkNet training complete: Autozoom_v10" "guppi" 

'''
message = sys.argv[1]
channel = sys.argv[2]

Guppi().send(message, channel)