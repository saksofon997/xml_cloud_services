import boto3
from boto3.dynamodb.conditions import Key


def create_table(db_items=[]):
    resource = boto3.resource("dynamodb", region_name="us-east-1")
    resource.create_table(
        TableName="xmlws-dev",
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
        ],
        BillingMode="PROVISIONED",
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

    table = resource.Table("xmlws-dev")

    if len(db_items) != 0:
        for it in db_items:
            table.put_item(Item=it)

    return table


def get_item(table, id, sk):
    return table.get_item(
        Key={
            "id": id,
            "sk": sk
        }
    )


def do_query(table, id, sk_prefix):
    response = table.query(
        KeyConditionExpression=Key("id").eq(id) & Key("sk").begins_with(sk_prefix)
    )
    return response
