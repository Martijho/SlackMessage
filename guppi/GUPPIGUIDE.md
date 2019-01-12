# GUPPI

### Setup
1. Download this repo and install requirements
```bash
git clone https://github.com/Martijho/SlackMessage.git
cd SlackMessage
pip install requirements.txt
```
2. Set Slackbot token as environment variable
    - Either create your own slack bot, set its access to your slack workplace or get hold of the token for an existing slack bot
    - export token
```bash
export guppi_api_token=*******************
source ~/.bashrc
```
3. Add bot to channel

4. Enjoy the benefit of your own General Unit Primary Peripheral Interface

### Example use
```python
from slackmessage import Guppi
guppi = Guppi()

# Sending message to channel
guppi.send('6345 items in to-do list',  # Message
           'testchannel')               # channel name

# Send file to channel
guppi.send_file('/home/MyUser/Desktop/totally_not_nudes.jpg',  # File path
                'totally_not_my_boss',                         # channel name
                message='Totally not asking for a promotion')  # string to preced file

# Send image to channel
import cv2
image = cv2.imread('/home/MyUser/Desktop/totally_not_nudes.jpg')
guppi.send_image(image,                 # image array 
                 'totally_not_HR',      # channel name
                 message='Im sorry')    # string to preced image
```