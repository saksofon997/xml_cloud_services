import json
from http import HTTPStatus


class Response(object):

    def __init__(self, status, body=None):
        self.status = status
        self.body = body

    def json(self):
        return {
            "statusCode": self.status,
            "body": json.dumps(self.body),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    @staticmethod
    def ok(body=None):
        return Response(HTTPStatus.OK, body).json()

    @staticmethod
    def accepted():
        return Response(HTTPStatus.ACCEPTED, None).json()

    @staticmethod
    def bad_request():
        return Response(HTTPStatus.BAD_REQUEST, None).json()

    @staticmethod
    def no_content():
        return Response(HTTPStatus.NO_CONTENT, None).json()
