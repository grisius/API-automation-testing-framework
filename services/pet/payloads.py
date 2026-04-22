from faker import Faker


fake = Faker()

class Payloads:

    add_new_pet_to_store = {
        "id": 1112223330212,
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

    update_pet_data = {
        "id": 1112223330212,
        "category": {
            "id": 552233617,
            "name": "cat_updated"
            },
        "name": "Buddy_updated",
        "photoUrls": [
            "www.buddy_updated.flow",
            "www.doggy_updated.com"
            ],
        "tags": [{
            "id": 42151,
            "name": "username_updated"
            }],
        "status": "available"
    }
