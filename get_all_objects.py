import requests
from endpoints.base_endpoint import Endpoint

class GetAllObjects(Endpoint):

    def get_all_objects(self):
        self.response = requests.get(f'https://api.restful-api.dev/objects')
        self.response_json = self.response.json()

