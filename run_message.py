from slack_sdk import WebClient
from settings import token

CHANNEL = "public"
TOKEN = token

def send_message(message):
    channel = CHANNEL
    token = TOKEN
    client = WebClient(token=token)
    client.chat_postMessage(channel=channel, text=message)

send_message(message="안녕하소~ 봇이여")