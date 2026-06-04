from api.user.payloads import Payloads as UserPayloads
from api.pet.payloads import Payloads as PetPayloads
from api.user.models.user_model import UserModel
from api.pet.models.pet_model import PetModel
from api.user.api_user import UserAPI
from api.pet.api_pet import PetAPI
from faker import Faker
import requests as r
import pytest
from dotenv import load_dotenv
import os


HOST_URL = "https://petstore.swagger.io/v2"
user_api = UserAPI()
pet_api = PetAPI()
fake = Faker("ru_Ru")
load_dotenv()

@pytest.fixture()
def created_user():
    payload = UserPayloads().user_random_data
    response = r.post(
        url=f"{HOST_URL}/user",
        json=payload
    )
    assert response.status_code == 200, response.text
    assert int(response.json()["message"]) == payload["id"]
    print("\nUser successfully created..")
    model = UserModel(**payload)
    yield model
    try:
        response = r.delete(url=f"{HOST_URL}/user/{model.username}")
        assert response.status_code == 200, response.text
    except AssertionError:
        assert response.status_code == 404, response.text
        response = r.get(url=f"{HOST_URL}/user/{model.username}")
        assert response.status_code == 404, response.text
        assert response.json()["message"] == "User not found"
        print("\nUser successfully deleted..")


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = r.post(
        url="https://petstore.swagger.io/oauth/authorize",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 200, f"Auth fail: {response.text}"


