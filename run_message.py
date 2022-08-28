from slack_sdk import WebClient
from settings import token

client = WebClient(token=token)

client.chat_postMessage(channel="public",
                        text="안녕하세요 봇입니다~")
