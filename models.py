from dataclasses import dataclass

@dataclass
class Location:
    lat: float
    lng: float
    address: str
    city: str 
    country: str 

    def merge(self, location):
        if self.lat == None:
            self.lat = location.lat

        if self.lng == None:
            self.lng = location.lng

        if self.address == None:
            self.address = location.address

        if self.city == None:
            self.city = location.city

        if self.country == None:
            self.country = location.country


@dataclass
class Amenities:
    general: list[str]
    room: list[str]

    def merge(self, amenities):
        self.general = list(set(self.general + amenities.general))
        self.room = list(set(self.room + amenities.room))
    
@dataclass
class Image:
    link: str
    description: str

    def merge(self, image):
        if self.link == None:
            self.link = location.link 

        if self.description == None:
            self.description = location.description 
    
    

@dataclass
class Images:
    rooms: list[Image]
    site: list[Image]
    amenities: list[Image]

    def merge(self, image):
        self.rooms = list(set(self.rooms + image.rooms))
        self.site = list(set(self.site + image.site))
        self.amenities = list(set(self.amenities + image.amenities))
        

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
        self.id = id or hotel.id
        self.destination_id = destination_id or hotel.destination_id
        self.name = name or hotel.name
        self.name = name or hotel.name
        self.name = name or hotel.name
        self.name = name or hotel.name
        self.name = name or hotel.name

    def to_string(self):
        return json.dumps(self, default=vars, indent=2)