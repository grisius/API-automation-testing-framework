from datetime import timezone
from faker import Faker


fake = Faker()

class Payloads:

    correct_order_data = {
        "id": fake.random_int(1, 10),
        "petId": fake.random_number(16),
        "quantity": 1,
        "shipDate": fake.iso8601(tzinfo=timezone.utc, timespec="minutes"),
        "status": "placed",
        "complete": True
    }

    invalid_order_data = {
        "id": 7,
        "petId": 7777888999933001,
        "quantity": 1,
        "shipDate": "2026-04-30Е14:46:42.338Z",
        "status": "placed",
        "complete": True
    }
