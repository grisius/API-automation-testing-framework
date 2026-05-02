from services.store.models.store_model import StoreModel, ApiResponseModel
from services.store.endpoints import Endpoints
from services.store.payloads import Payloads
from config.headers import Headers
from utils.helper import Helper
import requests as r
import pytest


class StoreAPI(Helper):

    def __init__(self):
        super().__init__()
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.status = ["available", "pending", "sold"]

    def get_pet_inventories(self):
        response = r.get(
            url=self.endpoints.get_pet_inventory_get
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return response.json()

    def check_get_pet_inventory(self, model):
        for s in self.status:
            assert s in model.keys(), model

    def place_order_for_a_pet(self):
        response = r.post(
            url=self.endpoints.place_order_for_pet_post,
            json=self.payloads.correct_order_data
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StoreModel(**response.json())
        return model

    def check_place_order_for_a_pet(self, model):
        assert model == StoreModel(
            **self.payloads.correct_order_data), model

    def get_purchase_order_by_id(self):
        order = self.place_order_for_a_pet()
        response = r.get(
            url=self.endpoints.get_order_by_id_get(order.id)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StoreModel(**response.json())
        return model

    def check_get_purchase_order_by_id(self, model):
        assert model == StoreModel(
            **self.payloads.correct_order_data), model

    def delete_purchase_order_by_id(self):
        order = self.place_order_for_a_pet()
        response = r.delete(
            url=self.endpoints.delete_order_by_id_delete(order.id)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    def check_delete_purchase_order_by_id(self, model):
        order_id = str(self.payloads.correct_order_data["id"])
        assert model.message == order_id




