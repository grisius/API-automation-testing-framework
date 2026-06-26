from faker import Faker


fake = Faker()

class Payloads:

    add_new_pet = {
        "id": fake.random_number(13),
        "category": {
            "id": fake.random_number(4),
            "name": fake.street_suffix()
            },
        "name": fake.name(),
        "photoUrls": [
            fake.url(),
            fake.url()
            ],
        "tags": [{
            "id": fake.random_number(3),
            "name": fake.user_name()
            }],
        "status": "available"
    }

    update_pet_data = {
        "id": add_new_pet["id"],
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

    incorrect_pet_data = {
        "id": 1112223330212222563236236233,
        "category": {
            "id": fake.random_number(4),
            "name": fake.street_suffix()
        },
        "tags": [{
            "id": fake.random_number(3),
            "name": fake.user_name()
        }],
        "status": "available"
    }
