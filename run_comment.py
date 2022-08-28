from slack_sdk import WebClient
from settings import token

class SlackAPI:
    """
    Slack API 핸들러
    """
    def __init__(self, token):
        self.client = WebClient(token)

    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        channels = result.data['channels']
        channel = list(filter(lambda c: c['name'] == channel_name, channels))[0]
        channel_id = channel['id']
        return channel_id
        
    def get_message_ts(self, channel_id, query):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data['messages']
        message = list(filter(lambda m: m['text'] == query, messages))[0] # 해당 문구 없으면 index out of range 에러 발생
        message_ts = message['ts']
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        result = self.client.chat_postMessage(
                channel=channel_id,
                text=text,
                thread_ts=message_ts
        )
        return result

slack = SlackAPI(token)

channel_name = "public"
query = "슬랙 봇 테스트 중입니다"
text = "자동 생성 문구 테스트"

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)
slack.post_thread_message(channel_id, message_ts, text)

