import json

from app.repository.LocationRepo import LocationRepo

repo = LocationRepo()


def handle(event, context):
    body = json.loads(event["Records"][0]["body"])

    token = body["token"]
    id = body["id"]
    coordinates = body["coordinates"]

    repo.add(id, token, coordinates)

    return True
