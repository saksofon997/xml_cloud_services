import sys
import time

import requests
from faker import Faker

faker = Faker()
Faker.seed(time.time())

while 1:
    time.sleep(5)

    coords = faker.local_latlng(country_code='RS', coords_only=True)

    lat = coords[0]
    long = coords[1]

    data = {
        "id": str(sys.argv[1]),
        "token": str(sys.argv[2]),
        "coordinates": {
            "lat": lat,
            "long": long
        }
    }

    print(data)

    response = requests.post(
        url="https://hsejfoit96.execute-api.us-east-1.amazonaws.com/dev/location",
        json=data
    )

    print(response.text)
