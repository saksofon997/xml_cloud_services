import pytest


@pytest.fixture()
def response_no_body():
    return {
        "statusCode": 200,
        "body": "null",
        "headers": {
            "Content-Type": "application/json"
        }
    }


@pytest.fixture()
def response():
    return {
        "statusCode": 200,
        "body": '{"test": "test"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }


def test_ok_no_body(response_no_body):
    from app.api.Response import Response

    ok_response = Response.ok()

    assert ok_response == response_no_body


def test_ok(response):
    from app.api.Response import Response

    body = {"test": "test"}

    ok_response = Response.ok(body)

    assert ok_response == response
