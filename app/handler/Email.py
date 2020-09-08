import json
import logging
import os

import boto3

from app.api.Response import Response

sqs = boto3.client('sqs')
queue_url = os.environ["EMAIL_QUEUE_URL"]


def handle(event, context):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=event["body"]
    )

    logging.info(f"Message {response['MessageId']} sent to Queue.")

    return Response.accepted()
