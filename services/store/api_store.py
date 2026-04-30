from services.store.models.store_model import StoreModel
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
