from config.base_test import BaseTest
import pytest
import allure


@allure.epic("User Module")
@allure.feature("Positive Cases")
@pytest.mark.positive
class TestUserPositive(BaseTest):

    @allure.story("User registration")
    @allure.title("Create user")
    def test_create_new_user(self):
        user = self.api_user.create_user()
        self.api_user.check_user_created(user)

    @allure.story("User profile management")
    @allure.title("Get user by username")
    def test_get_user_by_username(self, created_user):
        user = self.api_user.get_user_by_username(created_user.username)
        self.api_user.check_user_received_by_username(created_user, user)

    @allure.story("User authentication")
    @allure.title("Logs user in")
    def test_log_in_user(self, created_user):
        user = self.api_user.login_user(created_user)
        self.api_user.check_user_log_in(user)

    @allure.story("User profile management")
    @allure.title("Update user")
    def test_update_user(self, created_user):
        user = self.api_user.update_user(created_user.username)
        self.api_user.check_user_update(user)

    @allure.story("User authentication")
    @allure.title("Logs user out")
    def test_log_out_user(self, created_user):
        self.api_user.login_user(created_user)
        user = self.api_user.user_log_out()
        self.api_user.check_user_log_out(user)

    @allure.story("User profile management")
    @allure.title("Delete user")
    def test_delete_user(self, created_user):
        user = self.api_user.delete_user(created_user.username)
        self.api_user.check_delete_user(user)


@allure.epic("User Module")
@allure.feature("Negative Cases")
@pytest.mark.negative
class TestUserNegative(BaseTest):

    @allure.story("User registration")
    @allure.title("Create user with incorrect data")
    def test_create_user_with_incorrect_data(self):
        user = self.api_user.create_incorrect_user()
        self.api_user.check_user_not_created(user)

    @allure.story("User profile management")
    @allure.title("Get nonexistent user by username")
    def test_get_nonexistent_user_by_username(self):
        user = self.api_user.get_nonexistent_user_by_username()
        self.api_user.check_user_not_found_by_username(user)

    @allure.story("User authentication")
    @allure.title("Logs user in with incorrect data")
    @pytest.mark.xfail
    def test_log_in_user_with_incorrect_data(self):
        user = self.api_user.login_user_with_incorrect_data()
        self.api_user.check_user_not_log_in(user)
