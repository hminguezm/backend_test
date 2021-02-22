import sys
import logging

sys.path.insert(1, "./python-slackclient")
from slack import WebClient

logging.basicConfig(level=logging.DEBUG)
client = WebClient()
api_response = client.api_test()
