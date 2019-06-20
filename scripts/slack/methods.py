from botocore.vendored import requests
import os

URLS = {
    "postEphemeral": "https://slack.com/api/chat.postEphemeral",
    "filesUpload": "https://slack.com/api/files.upload",
    "dialogOpen": "https://slack.com/api/dialog.open"
}
HEADERS = {
    "Content-type": "application/json",
    "Authorization": "Bearer {}".format(os.environ['SLACKBOT_TOKEN'])
}


def postMessage(channel, user, **kwargs):
    requests.post(
        url=URLS['postEphemeral'],
        headers=HEADERS,
        json={
            "channel": channel,
            "user": user,
            "text": kwargs.get("text", ""),
            "blocks": kwargs.get("blocks", [])
        })


def dialogOpen(dialog, triggerId):
    requests.post(
        url=URLS['dialogOpen'],
        headers=HEADERS,
        json={
            "dialog": dialog,
            "trigger_id": triggerId
        })


def filesUpload(user, file, **kwargs):
    requests.post(
        url=URLS['filesUpload'],
        headers={
            "Authorization": "Bearer {}".format(os.environ['SLACKBOT_TOKEN'])
        },
        params={
            "channels": user,
            "filename": kwargs.get('filename', file)
        },
        files={
            "file": ('/tmp/' + file, open('/tmp/' + file, 'rb'), file.split('.')[-1])
        }
    )


def filesCreate(user, file):
    requests.post(
        url=URLS['filesUpload'],
        headers={
            "Authorization": "Bearer {}".format(os.environ['DATA_BOT_TOKEN'])
        },
        data={
            "channels": user,
            "content": open(file, 'r').read(),
            "filename": file,
            "filetype": file.split('.')[-1]
        }
    )


def response(code, message):
    return {
        "statusCode": str(code),
        "body": message,
        "headers": {
            "Content-Type": "application/json",
        }
    }
