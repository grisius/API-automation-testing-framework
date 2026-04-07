from config.base_test import BaseTest
import pytest


@pytest.mark.positive
class TestPet(BaseTest):

    def test_add_new_pet_to_store(self):
        pet = self.api_pet.add_new_pet_to_store()
        self.api_pet.check_pet_add_to_store(pet)

