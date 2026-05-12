from config.base_test import BaseTest
import pytest
import allure


@allure.epic("Pet Module")
@allure.feature("Positive Cases")
@pytest.mark.positive
class TestPet(BaseTest):

    @allure.story("Pet creation")
    @allure.title("Add a new pet to the store")
    def test_add_new_pet_to_store(self):
        pet = self.api_pet.add_new_pet_to_store()
        self.api_pet.check_pet_add_to_store(pet)

    @allure.story("Pet data retrieval")
    @allure.title("Get pet by ID")
    def test_get_pet_by_id(self):
        pet = self.api_pet.get_pet_by_id()
        self.api_pet.check_pet_get_by_id(pet)

    @allure.story("Data update")
    @allure.title("Update an existing pet")
    def test_update_existing_pet(self):
        pet = self.api_pet.update_existing_pet()
        self.api_pet.check_update_existing_pet(pet)

    @allure.story("Pet deletion")
    @allure.title("Deletes a pet")
    def test_delete_pet(self):
        pet = self.api_pet.delete_pet()
        self.api_pet.check_delete_pet(pet)


@allure.epic("Pet Module")
@allure.feature("Negative Cases")
@pytest.mark.negative
class TestPetNegative(BaseTest):

    @allure.story("Pet creation")
    @allure.title("Add a new pet with incorrect data")
    def test_add_new_pet_with_incorrect_data(self):
        pet = self.api_pet.add_new_pet_with_incorrect_data()
        self.api_pet.check_add_new_pet_with_incorrect_data(pet)

    @allure.story("Pet data retrieval")
    @allure.title("Get pet by nonexistent ID")
    def test_get_pet_by_nonexistent_id(self):
        pet = self.api_pet.get_pet_by_nonexistent_id()
        self.api_pet.check_get_pet_with_nonexistent_id(pet)

    @allure.story("Pet deletion")
    @allure.title("Deletes a nonexistent pet")
    def test_delete_nonexistent_pet(self):
        pet = self.api_pet.delete_nonexistent_pet()
        self.api_pet.check_delete_nonexistent_pet(pet)
