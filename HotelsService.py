from models import Hotel

class HotelsService:
    hotel_data: list[Hotel]

    def __init__(self):
        self.hotel_data = []

    def merge_and_save(self, all_supplier_data):
        all_supplier_data = all_supplier_data.sort(key=lambda hotel : hotel.id)
        self.hotel_data = all_supplier_data

    def find(self, hotel_ids, destination_ids):
        return self.hotel_data