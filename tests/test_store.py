from config.base_test import BaseTest


class TestStore(BaseTest):

    def test_get_pet_inventory(self):
        inventory = self.api_store.get_pet_inventories()
        self.api_store.check_get_pet_inventory(inventory)

    def test_place_order_for_a_pet(self):
        order = self.api_store.place_order_for_a_pet()
        self.api_store.check_place_order_for_a_pet(order)

    def test_get_purchase_order_by_id(self):
        order = self.api_store.get_purchase_order_by_id()
        self.api_store.check_get_purchase_order_by_id(order)

    def test_delete_purchase_order_by_id(self):
        order = self.api_store.delete_purchase_order_by_id()
        self.api_store.check_delete_purchase_order_by_id(order)
