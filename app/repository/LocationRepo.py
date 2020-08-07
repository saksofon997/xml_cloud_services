import boto3
from boto3.dynamodb.conditions import Key


class LocationRepo(object):
    VEHICLE_PREFIX = "VEHICLE_"

    def __init__(self):
        self.client = boto3.resource("dynamodb")
        self.table = self.client.Table("xmlws-dev")

    def add(self, id: str, token: str, coordinates: dict) -> bool:
        self.table.put_item(
            Item={
                "pk": id,
                "sk": f"{LocationRepo.VEHICLE_PREFIX}{token}",
                "coordinates": coordinates
            }
        )
        return True

    def find(self, id: str):
        response = self.table.query(
            KeyConditionExpression=Key("pk").eq(id) & Key("sk").begins_with(LocationRepo.VEHICLE_PREFIX)
        )
        coordinates = [x["coordinates"] for x in response["Items"]]
        return coordinates[0]
