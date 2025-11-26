from faker import Faker
from random import randint


fake = Faker()

class Payloads:

    add_new_pet_to_store = {
        "id": randint(11, 100),
        "category": {
            "id": randint(101, 200),
            "name": fake.street_suffix()
            },
        "name": fake.name(),
        "photoUrls": [
            fake.url()
            ],
        "tags": [{
            "id": randint(201, 300),
            "name": fake.user_name()
            }],
        "status": "available"
    }

print(Payloads().add_new_pet_to_store)
