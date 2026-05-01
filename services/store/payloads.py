from faker import Faker

fake = Faker()


class Payloads:

    correct_order_data = {
    "id": 7,
    "petId": 7777888999933001,
    "quantity": 1,
    "shipDate": "2026-04-30T14:46:42.338Z",
    "status": "placed",
    "complete": True
    }