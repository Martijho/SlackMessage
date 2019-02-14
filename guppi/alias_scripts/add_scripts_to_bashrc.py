import os
from os.path import expanduser

here = os.path.dirname(os.path.abspath(__file__))
home = expanduser("~")

with open(home + '/.bashrc', 'r') as bashrc:
    if '# guppi alias scripts' in bashrc.read():
        raise ValueError('Alias already in .bashrc')


with open(home + "/.bashrc", "a") as bashrc:
    bashrc.write("\n# guppi alias scripts \n")
    bashrc.write('alias guppi=\"python {}\" \n'.format(here+'/push_text_to_channel.py'))
    bashrc.write('alias guppi_file=\"python {}\" \n'.format(here + '/push_file_to_channel.py'))
    bashrc.write('alias guppi_image=\"python {}\" \n'.format(here + '/push_image_to_channel.py'))
