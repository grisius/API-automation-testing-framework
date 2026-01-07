
HOST_URL = "https://petstore.swagger.io/v2"

class Endpoints:

    add_new_pet_post = f"{HOST_URL}/pet"
    delete_pet = lambda self, petid: f"{HOST_URL}/pet/{petid}"
    upload_pet_image_post = lambda self, petid: f"{HOST_URL}/pet/{petid}/uploadImage"
    find_pet_by_status_get = f"{HOST_URL}/pet/findByStatus"
    find_pet_by_id_get = lambda self, petid: f"{HOST_URL}/pet/{petid}"
    update_an_existing_pet_put = f"{HOST_URL}/pet"
