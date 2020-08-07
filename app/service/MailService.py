import json

from app.external.MailProxy import MailProxy


def handle(event, context):
    body = json.loads(event["Records"][0]["body"])

    address = body["address"]
    message = body["message"]

    MailProxy().send(toaddrs=address, message=message)

    return True
