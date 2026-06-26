from api.user.models.user_model import UserModel, ApiResponseModel
from api.user.payloads import Payloads
from api.user.endpoints import Endpoints
from config.headers import Headers
from utils.helper import Helper
import requests as r
import allure


class UserAPI(Helper):

    def __init__(self):
        super().__init__()
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.user_data = UserModel(**self.payloads.user_random_data)

    @allure.step("Create user")
    def create_user(self):
        response = r.post(
            url=self.endpoints.create_user_post,
            headers=self.headers.basic,
            json=self.payloads.user_random_data
        )
        assert response.status_code == 200, \
            f"Fail creating user: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step("Check user created")
    def check_user_created(self, response):
        assert response.message == str(self.user_data.id), \
            f"User id is not correct: {response.message}"
        print(response)

    @allure.step("Get user by username")
    def get_user_by_username(self, username):
        response = r.get(
            url=self.endpoints.get_user_by_username_get(username)
        )
        assert response.status_code == 200, \
            f"Fail getting user by username: {response.json()}"
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @staticmethod
    @allure.step("Check user received by username")
    def check_user_received_by_username(response, user):
        assert response.id == user.id, \
            f"wrong id: {response.id}"
        assert response.username == user.username, \
            f"wrong username: {response.username}"

    @allure.step("Login user")
    def login_user(self, user):
        params = {"username": user.username, "password": user.password}
        response = r.get(
            url=self.endpoints.log_in_user_get,
            params=params
        )
        assert response.status_code == 200, \
            f"Fail login user: {response.json()}"
        assert response.headers["x-rate-limit"] == "5000", response.json()
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    @allure.step("Check user log in")
    def check_user_log_in(response):
        assert "logged in user" in response.message, "Fail login user"

    @allure.step("Update user")
    def update_user(self, username):
        user_update = r.put(
            url=self.endpoints.update_user_put(username),
            json=self.payloads.update_user,
        )
        assert user_update.status_code == 200, \
            f"Fail update user: {user_update.json()}"
        self.attach_response(user_update.json())
        model = ApiResponseModel(**user_update.json())
        return model

    @allure.step("Check user update")
    def check_user_update(self, response):
        assert response.message == "7777777000000"
        response = r.get(
            url=self.endpoints.get_user_by_username_get(
                self.payloads.update_user["username"])
        )
        assert response.json() == self.payloads.update_user, \
            f"Fail user update: {response.json()}"


    @allure.step("User log out")
    def user_log_out(self):
        response = r.get(
            url=self.endpoints.log_out_user_get
        )
        assert response.status_code == 200, \
            f"Fail user log out: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @staticmethod
    @allure.step("Check user log out")
    def check_user_log_out(response):
        assert response.message == "ok", \
            f"Fail user log out: {response.json()}"

    @allure.step("Delete user")
    def delete_user(self, username):
        response = r.delete(
            url=self.endpoints.delete_user(username)
        )
        assert response.status_code == 200, \
            f"Fail delete user: {response.json()}"
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step("Check delete user")
    def check_delete_user(self, username):
        response = r.get(
            url=self.endpoints.get_user_by_username_get(username)
        )
        assert response.status_code == 404, response.json()
        assert response.json()["message"] == "User not found", \
            f"Incorrect delete user message: {response}"


    # Negative

    @allure.step("Create incorrect user")
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
    @allure.step("Check user not created")
    def check_user_not_created(response):
        assert response.message == "something bad happened", \
            f"User created: {response.message}"

    @allure.step("Get nonexistent user by username")
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
    @allure.step("Check user not found by username")
    def check_user_not_found_by_username(response):
        assert response.message == "User not found", \
            f"wrong message: {response.message}"

    @allure.step("Login user with incorrect data")
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
    @allure.step("Check user not log in")
    def check_user_not_log_in(response):
        assert response.message == "Invalid username/password supplied", \
            "Wrong message"
