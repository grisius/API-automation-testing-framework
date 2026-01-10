from services.pet.models.pet_model import PetModel
from services.pet.endpoints import Endpoints
from services.pet.payloads import Payloads
from config.headers import Headers
from utils.helper import Helper
import requests as r
import allure


class PetAPI(Helper):

    def __init__(self):
        super().__init__()
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Add new pet to store")
    def add_new_pet_to_store(self):
        response = r.post(
            url=self.endpoints.add_new_pet_post,
            headers=self.headers.basic,
            json=self.payloads.add_new_pet_to_store
        )
        assert response.status_code == 200, f"Response json: \n{response.json()}"
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model
