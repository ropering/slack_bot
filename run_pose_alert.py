"""
참고자료
- https://dragon1-honey1-wayfarer.tistory.com/entry/Python-%EC%8A%AC%EB%9E%99Slack-%EC%95%8C%EB%A6%BC%EB%B4%87-%EC%84%A4%EC%A0%95%ED%95%98%EC%97%AC-%EB%A7%A4%EC%9D%BC-%EC%A6%9D%EC%8B%9C-%EC%95%8C%EB%A6%BC-%EB%B0%9B%EA%B8%B0-2?category=892038
- https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC+apscheduler&sourceid=chrome&ie=UTF-8
"""

from slack_sdk import WebClient
from settings import token


# attachment에 들어갈 내용
title = "제목"
title_link = "https://dragon1-honey1-wayfarer.tistory.com/entry/Python-%EC%8A%AC%EB%9E%99Slack-%EC%95%8C%EB%A6%BC%EB%B4%87-%EC%84%A4%EC%A0%95%ED%95%98%EC%97%AC-%EB%A7%A4%EC%9D%BC-%EC%A6%9D%EC%8B%9C-%EC%95%8C%EB%A6%BC-%EB%B0%9B%EA%B8%B0-2?category=892038"
text = "내용"
image_url = "https://noticon-static.tammolo.com/dgggcrkxq/image/upload/v1586271210/noticon/sageach1qrmmyfufwli1.gif"

attach_dict = {
    'color' : '#ff0000',
    'author_name' : '오명균',
    'title' : title,
    'title_link' : title_link,
    'text' : text,
    'image_url' : image_url,
}

block_dict = {
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"
  }
}


class SlackAPI(object):
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
        message = list(filter(lambda m: m['text'] == query, messages))[0]
        message_ts = message['ts']
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text, attach_dict):
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text,
            # thread_ts=message_ts,
            attachments=attach_dict,
            # blocks=block_dict,
        )
        return result

slack = SlackAPI(token)

channel_name = "public"
query = "슬랙 봇 테스트 중입니다"
text = "하이 \n 명균 \n 반가워"

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)

attach_dict = [attach_dict]
slack.post_thread_message(channel_id, message_ts, text, attach_dict)

