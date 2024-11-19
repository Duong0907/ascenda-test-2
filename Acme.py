from BaseSupplier import BaseSupplier 
from models import Hotel, Location, Amenities, Images, Image 

class Acme(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto['Id'].strip(),
            destination_id=dto['DestinationId'],
            name=dto['Name'].strip(),
            description=dto['Description'].strip(),
            location=Location(
                lat=dto['Latitude'],
                lng=dto['Longitude'],
                address=dto['Address'].strip(),
                city= dto['City'].strip(),
                country= dto['Country'].strip()
            ),
            amenities=Amenities(
                general=dto['Facilities'],
                room=None
            ),
            images=None,
            booking_conditions=None
        )