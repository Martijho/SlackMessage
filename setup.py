from setuptools import setup, find_packages

setup(
  name='slackmessage',
  version='1.0',
  description='Send slack messages to myself',
  author='Martin Hovin',
  author_email='MartinHovin91@gmail.com',
  url='https://github.com/Martijho/SlackMessage',
  packages=['slackmessage']#find_packages(exclude=('test',)),
)
