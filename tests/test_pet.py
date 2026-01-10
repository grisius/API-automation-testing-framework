import pytest

from config.base_test import BaseTest
import allure


@allure.feature("Pet")
class TestPet(BaseTest):

    @pytest.mark.regression
    @allure.title("Add new pet to store")
    def test_add_new_pet_to_store(self):
        pet = self.api_pet.add_new_pet_to_store()
        print(pet.name, pet.category.id, pet.category.name, sep="\n")
