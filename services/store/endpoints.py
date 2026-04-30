
HOST_URL = "https://petstore.swagger.io/v2"

class Endpoints:

    get_pet_inventory_get = f"{HOST_URL}/store/inventory"
    place_order_for_pet_post = f"{HOST_URL}/store/order"
    get_order_by_orderid_get = lambda self, order_id: \
        f"{HOST_URL}/store/order/{order_id}"
    delete_order_by_orderid_delete = lambda self, order_id: \
        f"{HOST_URL}/store/order/{order_id}"