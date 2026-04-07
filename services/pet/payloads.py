from faker import Faker


fake = Faker()

class Payloads:

    add_new_pet_to_store = {
        "id": fake.random_number(5),
        "category": {
            "id": fake.random_number(4),
            "name": fake.street_suffix()
            },
        "name": "Buddy",
        "photoUrls": [
            "www.buddy.flow",
            "www.doggy.com"
            ],
        "tags": [{
            "id": fake.random_number(3),
            "name": fake.user_name()
            }],
        "status": "available"
    }
