from config.base_test import BaseTest
import pytest
import allure


@allure.epic("Store Module")
@allure.feature("Positive Cases")
@pytest.mark.positive
class TestStore(BaseTest):

    @allure.story("Inventory")
    @allure.title("Returns pet inventories by status")
    def test_get_pet_inventory(self):
        inventory = self.api_store.get_pet_inventory()
        self.api_store.check_get_pet_inventory(inventory)

    @allure.story("Order placement")
    @allure.title("Place an order for a pet")
    def test_place_order_for_a_pet(self):
        order = self.api_store.place_order_for_a_pet()
        self.api_store.check_place_order_for_a_pet(order)

    @allure.story("Order search")
    @allure.title("Get purchase order by ID")
    def test_get_purchase_order_by_id(self, created_order):
        order = self.api_store.get_purchase_order_by_id(created_order.id)
        self.api_store.check_get_purchase_order_by_id(order)

    @allure.story("Order deletion")
    @allure.title("Delete purchase order by ID")
    def test_delete_purchase_order_by_id(self, created_order):
        order = self.api_store.delete_purchase_order_by_id(created_order.id)
        self.api_store.check_delete_purchase_order_by_id(order)


@allure.epic("Store Module")
@allure.feature("Negative Cases")
@pytest.mark.negative
class TestStoreNegative(BaseTest):

    @allure.story("Order placement")
    @allure.title("Place an invalid order for a pet")
    def test_place_invalid_order_for_a_pet(self):
        order = self.api_store.place_invalid_order_for_a_pet()
        self.api_store.check_place_invalid_order_for_a_pet(order)

    @allure.story("Order search")
    @allure.title("Get purchase order by invalid ID")
    def test_get_purchase_order_by_invalid_id(self):
        order = self.api_store.get_purchase_order_by_invalid_id()
        self.api_store.check_get_purchase_order_by_invalid_id(order)
