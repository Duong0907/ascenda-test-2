import requests
from models import Hotel

class BaseSupplier:
    def endpoint():
        pass

    def parse(obj: dict) -> Hotel:
        pass

    def fetch(self):
        url = self.endpoint()
        resp = requests.get(url)
        return [self.parse(dto) for dto in resp.json()]


