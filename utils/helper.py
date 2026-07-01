from allure_commons.types import AttachmentType as Atype
import json
import allure


class Helper:

    @staticmethod
    def attach_response(response) -> None:
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=Atype.JSON)