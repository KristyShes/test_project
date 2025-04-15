import allure
import requests
from endpoints.base_endpoint import Endpoint

class PatchObject(Endpoint):

    def patch_object_by_id(self, object_id, payload):
        self.response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=payload)
        self.response_json = self.response.json()

    def check_response_name(self, name):
        with allure.step('check update object'):
            assert self.response_json['name'] == name