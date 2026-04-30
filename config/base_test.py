from services.pet.api_pet import PetAPI
from services.user.api_user import UserAPI
from services.store.api_store import StoreAPI


class BaseTest:

    def setup_method(self):

        self.api_pet = PetAPI()
        self.api_user = UserAPI()
        self.api_store = StoreAPI()
        

