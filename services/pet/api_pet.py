from services.pet.models.pet_model import PetModel, ApiResponseModel
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
        self.incorrect_id = 9991112241001209
        self.name = "Buddy"
        self.photo_urls = [
            "www.buddy.flow",
            "www.doggy.com"
            ]

    @allure.step("Add new pet to store")
    def add_new_pet_to_store(self):
        response = r.post(
            url=self.endpoints.add_new_pet_post,
            headers=self.headers.basic,
            json=self.payloads.add_new_pet_to_store
        )
        assert response.status_code == 200, \
            f"Response json: \n{response.json()}"
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    def check_pet_add_to_store(self, pet):
        assert pet.name == self.name
        assert pet.photoUrls == self.photo_urls

    def get_pet_by_id(self):
        pet = self.add_new_pet_to_store()
        self.check_pet_add_to_store(pet)
        response = r.get(
            url=self.endpoints.find_pet_by_id_get(pet.id),
        )
        assert response.status_code == 200, \
            f"Response json: \n{response.json()}"
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    def check_pet_get_by_id(self, pet):
        assert pet.name == self.name
        assert pet.photoUrls == self.photo_urls

    def update_existing_pet(self):
        pet = self.add_new_pet_to_store()
        self.check_pet_add_to_store(pet)
        response = r.put(
            url=self.endpoints.update_an_existing_pet_put,
            json=self.payloads.update_pet_data
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    def check_update_existing_pet(self, pet):
        assert pet == PetModel(**self.payloads.update_pet_data), \
            f"model is not correct: {pet}"

    def delete_pet(self):
        pet = self.add_new_pet_to_store()
        self.check_pet_add_to_store(pet)
        response = r.delete(
            url=self.endpoints.delete_pet(pet.id)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    def check_delete_pet(self, pet):
        pet_id = int(pet.message)
        response = r.get(
            url=self.endpoints.find_pet_by_id_get(pet_id))
        assert response.status_code == 404, response.json()
        assert response.json()["message"] == "Pet not found", \
            response.json()

    # Negative

    def add_new_pet_with_incorrect_data(self):
        response = r.post(
            url=self.endpoints.add_new_pet_post,
            json=self.payloads.incorrect_pet_data
        )
        assert response.status_code == 500, response.json()
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_add_new_pet_with_incorrect_data(pet):
        assert pet.message == "something bad happened", pet

    def get_pet_by_nonexistent_id(self):
        response = r.get(
            url=self.endpoints.find_pet_by_id_get(self.incorrect_id))
        assert response.status_code == 404, response.json()
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_get_pet_with_nonexistent_id(pet):
        assert pet.message == "Pet not found", pet

    def delete_nonexistent_pet(self):
        response = r.delete(
            url=self.endpoints.delete_pet(self.incorrect_id),
            headers=self.headers.basic
        )
        assert response.status_code is not 200, response
        return response

    @staticmethod
    def check_delete_nonexistent_pet(pet):
        assert pet.status_code == 404, pet
