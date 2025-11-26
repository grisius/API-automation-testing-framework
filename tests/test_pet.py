from config.base_test import BaseTest


class TestPet(BaseTest):

    def test_add_new_pet_to_store(self):
        pet = self.api_pet.add_new_pet_to_store()
        print(pet.name, pet.category.id, pet.category.name, sep="\n")
