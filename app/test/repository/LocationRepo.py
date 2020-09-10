import pytest

from app.repository.LocationRepo import LocationRepo
from moto import mock_dynamodb2
from app.test.utils.DynamoDB import create_table, get_item


@pytest.fixture
def item():
    return {
        "id": "12345",
        "sk": "VEHICLE_foobar",
        "coordinates": {
            "lat": "44.22639",
            "long": "22.53083"
        }
    }

@mock_dynamodb2
def test_add(item):
    table = create_table([item])

    repo = LocationRepo()

    repo.add(
        "12345",
        "foobar",
        {
            "lat": "44.22639",
            "long": "22.53083"
        }
    )

    test = get_item(table, "12345", "VEHICLE_foobar")

    assert test["Item"]["id"] is "12345"
    assert test["Item"]["sk"] is "VEHICLE_foobar"


@mock_dynamodb2
def test_find(item):
    create_table([item])

    repo = LocationRepo()

    coords = repo.find("12345")

    assert item["coordinates"] == coords
