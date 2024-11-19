from BaseSupplier import BaseSupplier 
from models import Hotel, Location, Amenities, Images, Image 

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
