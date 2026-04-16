from services.user.models.user_model import UserModel, ApiResponseModel
from services.user.payloads import Payloads
from services.user.endpoints import Endpoints
from config.headers import Headers
from utils.helper import Helper
import requests as r


class UserAPI(Helper):

    def __init__(self):
        super().__init__()
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.username = "crocodilo"
        self.nonexistent_user = "qwwrrr2rrrw222a"

    def create_user(self):
        response = r.post(
            url=self.endpoints.create_user_post,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, \
            f"Fail creating user: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_created(response):
        assert response.message == "111555999", \
            f"User id is not correct: {response.message}"

    def get_user_by_username(self):
        user = self.create_user()
        self.check_user_created(user)
        response = r.get(
            url=self.endpoints.get_user_by_username_get(self.username)
        )
        assert response.status_code == 200, \
            f"Fail getting user by username: {response.json()}"
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    def check_user_received_by_username(self, response):
        assert response.id == 111555999, \
            f"wrong id: {response.id}"
        assert response.username == self.username, \
            f"wrong username: {response.username}"

    def login_user(self):
        api_response = self.create_user()
        self.check_user_created(api_response)
        user = self.get_user_by_username()
        params = {"username": user.username, "password": user.password}
        response = r.get(
            url=self.endpoints.log_in_user_get,
            params=params
        )
        assert response.status_code == 200, \
            f"Fail login user: {response.json()}"
        assert response.headers["x-rate-limit"] == "5000"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_log_in(response):
        assert "logged in user" in response.message, "Fail login user"

    def update_user(self):
        api_response = self.create_user()
        self.check_user_created(api_response)
        user_update = r.put(
            url=self.endpoints.update_user_put(self.username),
            json=self.payloads.update_user,
        )
        assert user_update.status_code == 200, \
            f"Fail update user: {user_update.json()}"
        self.attach_response(user_update.json())
        model = ApiResponseModel(**user_update.json())
        return model

    def check_user_update(self, response):
        assert response.message == "7777777000000"
        response = r.get(
            url=self.endpoints.get_user_by_username_get("crocodilo-upd")
        )
        assert response.json() == self.payloads.update_user, \
            f"Fail user update: {response.json()}"

    def user_log_out(self):
        api_response = self.create_user()
        self.check_user_created(api_response)
        api_response = self.login_user()
        self.check_user_log_in(api_response)
        response = r.get(
            url=self.endpoints.log_out_user_get
        )
        assert response.status_code == 200, \
            f"Fail user log out: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_log_out(response):
        assert response.message == "ok", \
            f"Fail user log out: {response.json()}"

    def delete_user(self):
        api_response = self.create_user()
        self.check_user_created(api_response)
        user = self.get_user_by_username()
        response = r.delete(
            url=self.endpoints.delete_user(user.username)
        )
        assert response.status_code == 200, \
            f"Fail delete user: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    def check_delete_user(self, model):
        assert model.message == self.username, \
            f"Incorrect delete user message: {model}"
        response = r.get(
            url=self.endpoints.get_user_by_username_get(self.username)
        )
        assert response.status_code == 404, response.json()
        assert response.json()["message"] == "User not found"


    # Nagative

    def create_incorrect_user(self):
        response = r.post(
            url=self.endpoints.create_user_post,
            headers=self.headers.basic,
            json=self.payloads.incorrect_data
        )
        assert response.status_code == 500, \
            f"Fail creating user: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_not_created(response):
        assert response.message == "something bad happened", \
            f"User created: {response.message}"

    def get_nonexistent_user_by_username(self):
        response = r.get(
            url=self.endpoints.get_user_by_username_get("asdfgh99321xxw")
        )
        assert response.status_code == 404, \
            f"User exist: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_not_found_by_username(response):
        assert response.message == "User not found", \
            f"wrong message: {response.message}"

    def login_user_with_incorrect_data(self):
        params = {"username": "asfgh9321xw", "password": "wqqw2c3"}
        response = r.get(
            url=self.endpoints.log_in_user_get,
            params=params
        )
        assert response.status_code == 400, \
            f"Fail login user: {response.json()}"
        assert response.headers["x-rate-limit"] == "5000"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    def check_user_not_log_in(response):
        assert response.message == "Invalid username/password supplied", \
            "Wrong message"

