from config.base_test import BaseTest
import pytest


@pytest.mark.positive
class TestPet(BaseTest):

    def test_add_new_pet_to_store(self):
        pet = self.api_pet.add_new_pet_to_store()
        self.api_pet.check_pet_add_to_store(pet)

    def test_get_pet_by_id(self):
        pet = self.api_pet.get_pet_by_id()
        self.api_pet.check_pet_get_by_id(pet)

    def test_update_existing_pet(self):
        pet = self.api_pet.update_existing_pet()
        self.api_pet.check_update_existing_pet(pet)

    def test_delete_pet(self):
        pet = self.api_pet.delete_pet()
        self.api_pet.check_delete_pet(pet)


@pytest.mark.negative
class TestPetNegative(BaseTest):

    def test_add_new_pet_with_incorrect_data(self):
        pet = self.api_pet.add_new_pet_with_incorrect_data()
        self.api_pet.check_add_new_pet_with_incorrect_data(pet)

    def test_get_pet_by_nonexistent_id(self):
        pet = self.api_pet.get_pet_by_nonexistent_id()
        self.api_pet.check_get_pet_with_nonexistent_id(pet)

    def test_delete_nonexistent_pet(self):
        pet = self.api_pet.delete_nonexistent_pet()
        self.api_pet.check_delete_nonexistent_pet(pet)