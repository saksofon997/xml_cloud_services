import logging

from app.api.Response import Response
from app.repository.LocationRepo import LocationRepo

repo = LocationRepo()


def handle(event, context):
    try:
        id = str(event["queryStringParameters"]["id"])

        coords = repo.find(id)

        return Response.ok(coords)
    except Exception as e:
        logging.error(f"Locating vehicle failed due to {e}.")
