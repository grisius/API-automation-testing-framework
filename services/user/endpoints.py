
HOST_URL = "https://petstore.swagger.io/v2"

class Endpoints:

    create_user_post = f"{HOST_URL}/user"
    create_list_of_users_post = f"{HOST_URL}/user/createWithList"
    log_in_user_get = f"{HOST_URL}/user/login"
    log_out_user_get = f"{HOST_URL}/user/logout"
    get_user_by_username_get = lambda self, username: f"{HOST_URL}/user/{username}"
    update_user_put = lambda self, username: f"{HOST_URL}/user/{username}"
    delete_user = lambda self, username: f"{HOST_URL}/user/{username}"
