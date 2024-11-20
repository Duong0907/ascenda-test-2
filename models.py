from dataclasses import dataclass
from utils import merge_two_list, merge_two_value

@dataclass
class Location:
    lat: float
    lng: float
    address: str
    city: str 
    country: str 

    def merge(self, location):
        self.lat = merge_two_value(self.lat, location.lat)
        self.lng = merge_two_value(self.lng, location.lng)
        self.address = merge_two_value(self.address, location.address)
        self.city = merge_two_value(self.city, location.city)
        self.country = merge_two_value(self.country, location.country)


@dataclass
class Amenities:
    general: list[str]
    room: list[str]

    def merge(self, amenities):
        self.general = merge_two_list(self.general, amenities.general)
        self.room = merge_two_list(self.room, amenities.room)
    

@dataclass
class Image:
    link: str
    description: str

    def merge(self, image):
        self.link = merge_two_value(self.link, location.link) 
        self.description = merge_two_value(self.description, location.description) 
    

@dataclass
class Images:
    rooms: list[Image]
    site: list[Image]
    amenities: list[Image]

    def __init__(self, rooms=[], site=[], amenities=[]):
        self.rooms = rooms
        self.site = site
        self.amenities = amenities


    def merge(self, images):
        self.rooms = merge_two_list(self.rooms, images.rooms)
        self.site = merge_two_list(self.site, images.site)
        self.amenities = merge_two_list(self.amenities, images.amenities)
        

@dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    description: str
    location: Location
    amenities: Amenities
    images: Images
    booking_conditions: list[str]

    def merge(self, hotel):
        self.id = merge_two_value(self.id, hotel.id)
        self.destination_id = merge_two_value(self.destination_id, hotel.destination_id)
        self.name = merge_two_value(self.name, hotel.name)
        self.description = merge_two_value(self.description, hotel.description)

        self.location.merge(hotel.location)
        self.amenities.merge(hotel.amenities)
        self.images.merge(hotel.images)

        self.booking_conditions = merge_two_list(self.booking_conditions, hotel.booking_conditions)