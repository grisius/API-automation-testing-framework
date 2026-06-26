from faker import Faker

fake = Faker("ru_RU")


class Payloads:

    create_user = {
        "id": 111555999,
        "username": "crocodilo",
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": fake.random_number(3)
    }

    user_random_data = {
        "id": fake.random_number(9),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": fake.random_number(3)
    }

    update_user = {
        "id": 7777777000000,
        "username": "crocodilo-upd",
        "firstName": "updFName",
        "lastName": "updLName",
        "email": "upd-email@mail.hyz",
        "password": "upd-pswrd",
        "phone": "upd-phone",
        "userStatus": 111
    }

    incorrect_data = {
        "id": fake.random_number(7),
        "username": "crocodilo",
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": fake.random_number(10)
    }