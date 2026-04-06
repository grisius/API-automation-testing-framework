from config.base_test import BaseTest


class TestUser(BaseTest):

    def test_create_new_user(self):
        user = self.api_user.create_user()
        self.api_user.check_user_created(user)

    def test_get_user_by_username(self):
        user = self.api_user.get_user_by_username(self.api_user.username)
        self.api_user.check_user_received_by_username(user)

    def test_log_in_user(self):
        user_login = self.api_user.login_user()
        self.api_user.check_user_log_in(user_login)

    def test_update_user(self):
        user = self.api_user.update_user()
        self.api_user.check_user_update(user)

    def test_log_out_user(self):
        user = self.api_user.user_log_out()
        self.api_user.check_user_log_out(user)

