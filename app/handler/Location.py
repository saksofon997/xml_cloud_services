import json
import logging
import os

import boto3

from app.api.Response import Response

sqs = boto3.client('sqs')
queue_url = os.environ["LOCATION_QUEUE_URL"]


def handle(event, context):
    body = json.loads(event["body"])

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(body)
    )

    logging.info(f"Message {response['MessageId']} sent to Queue")

    return Response.accepted()
