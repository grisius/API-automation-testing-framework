from config.base_test import BaseTest


class TestStore(BaseTest):

    def test_get_pet_inventory(self):
        inventory = self.api_store.get_pet_inventories()
        self.api_store.check_get_pet_inventory(inventory)