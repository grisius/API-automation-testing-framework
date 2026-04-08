from config.base_test import BaseTest
import pytest


@pytest.mark.positive
class TestUserPositive(BaseTest):

    def test_create_new_user(self):
        user = self.api_user.create_user()
        self.api_user.check_user_created(user)

    def test_get_user_by_username(self):
        user = self.api_user.get_user_by_username()
        self.api_user.check_user_received_by_username(user)

    def test_log_in_user(self):
        user = self.api_user.login_user()
        self.api_user.check_user_log_in(user)

    def test_update_user(self):
        user = self.api_user.update_user()
        self.api_user.check_user_update(user)

    def test_log_out_user(self):
        user = self.api_user.user_log_out()
        self.api_user.check_user_log_out(user)

    def test_delete_user(self):
        user = self.api_user.delete_user()
        self.api_user.check_delete_user(user)


@pytest.mark.negative
class TestUserNegative(BaseTest):

    def test_create_user_with_incorrect_data(self):
        user = self.api_user.create_incorrect_user()
        self.api_user.check_user_not_created(user)

    def test_get_nonexistent_user_by_username(self):
        user = self.api_user.get_nonexistent_user_by_username()
        self.api_user.check_user_not_found_by_username(user)

    @pytest.mark.xfail
    def test_log_in_user_with_incorrect_data(self):
        user = self.api_user.login_user_with_incorrect_data()
        self.api_user.check_user_not_log_in(user)