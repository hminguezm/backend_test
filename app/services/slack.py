import os
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(
    token=os.environ.get('SLACK_API_TOKEN')
)


def send_to_slack(channel: str, message: str):
    print(channel)
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
        assert response["message"]["message"] == message
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")
