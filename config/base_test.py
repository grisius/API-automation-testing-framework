from services.pet.api_pet import PetAPI


class BaseTest:

    def setup_method(self):

        self.api_pet = PetAPI()
        

