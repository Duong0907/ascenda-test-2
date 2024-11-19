from BaseSupplier import BaseSupplier 
from models import Hotel, Location, Amenities, Images, Image 

class Paperflies(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        rooms = [Image(room['link'], room['caption']) for room in dto['images']['rooms']]
        site = [Image(site['link'], site['caption']) for site in dto['images']['site']]

        return Hotel(
            id=dto['hotel_id'].strip(),
            destination_id=dto['hotel_id'],
            name=dto['hotel_name'].strip(),
            description=dto['details'].strip(),
            location=Location(
                lat=None,
                lng=None,
                address=dto['location']['address'].strip(),
                city=None,
                country=dto['location']['country'].strip()
            ),
            amenities=Amenities(
                general=dto['amenities']['general'],
                room=dto['amenities']['room']
            ),
            images=Images(
                rooms=rooms,
                site=site,
                amenities=None
            ),
            booking_conditions=dto['booking_conditions']
        )
