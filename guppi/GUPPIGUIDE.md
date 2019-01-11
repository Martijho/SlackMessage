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
guppi.send('6345 items in to-do list', 'testchannel'

# Send file to channel
guppi.send_file('/home/MyUser/Desktop/totally_not_nudes.jpg', 'totally_not_my_boss', message='Totally not asking for a promotion')

# Send image to channel
import cv2
image = cv2.imread('/home/MyUser/Desktop/totally_not_nudes.jpg')
guppi.send_image(image, 'totally_not_HR', message='Im sorry')
```