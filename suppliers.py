import requests
from models import Hotel, Location, Amenities, Images, Image 

class BaseSupplier:
    def endpoint():
        pass

    def parse(obj: dict) -> Hotel:
        pass

    def fetch(self):
        url = self.endpoint()
        resp = requests.get(url)
        return [self.parse(dto) for dto in resp.json()]


class Acme(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto['Id'],
            destination_id=dto['DestinationId'],
            name=dto['Name'],
            description=dto['Description'],
            location=Location(
                lat=dto['Latitude'],
                lng=dto['Longitude'],
                address=dto['Address'],
                city= dto['City'],
                country= dto['Country']
            ),
            amenities=Amenities(
                general=dto['Facilities'],
                room=[]
            ),
            images=Images(),
            booking_conditions=[]
        )


class Paperflies(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        rooms = [Image(room['link'], room['caption']) for room in dto['images']['rooms']]
        site = [Image(site['link'], site['caption']) for site in dto['images']['site']]

        return Hotel(
            id=dto['hotel_id'],
            destination_id=dto['hotel_id'],
            name=dto['hotel_name'],
            description=dto['details'],
            location=Location(
                lat=None,
                lng=None,
                address=dto['location']['address'],
                city=None,
                country=dto['location']['country']
            ),
            amenities=Amenities(
                general=dto['amenities']['general'],
                room=dto['amenities']['room']
            ),
            images=Images(
                rooms=rooms,
                site=site,
                amenities=[]
            ),
            booking_conditions=dto['booking_conditions']
        )



class Patagonia(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        rooms = [Image(room['url'], room['description']) for room in dto['images']['rooms']]
        amenities = [Image(site['url'], site['description']) for site in dto['images']['amenities']]

        return Hotel(
            id=dto['id'],
            destination_id=dto['destination'],
            name=dto['name'],
            description=dto['info'],
            location=Location(
                lat=dto['lat'],
                lng=dto['lng'],
                address=dto['address'],
                city=None,
                country=None
            ),
            amenities=Amenities(
                general=dto['amenities'] if dto['amenities'] else [],
                room=[]
            ),
            images=Images(
                rooms=rooms,
                site=[],
                amenities=amenities
            ),
            booking_conditions=[]
        )
