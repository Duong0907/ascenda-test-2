from models import Hotel
import json

class HotelsService:
    hotel_data: list[Hotel]

    def __init__(self):
        self.hotel_data = []

    def merge_and_save(self, all_supplier_data):
        all_supplier_data.sort(key=lambda hotel: hotel.id)

        curr = all_supplier_data[0]
        i = 1

        while i < len(all_supplier_data):
            if curr.id == all_supplier_data[i].id:
                curr.merge(all_supplier_data[i])
            else:
                self.hotel_data.append(curr)
                curr = all_supplier_data[i]

            i += 1
            if curr.id == None:
                print(i)

        if curr not in self.hotel_data:
            self.hotel_data.append(curr)
        # print(json.dumps(self.hotel_data, default=vars, indent=2))

    def find(self, hotel_ids, destination_ids):
        if hotel_ids == "none" or destination_ids == "none":
            return self.hotel_data

        result = []
        hotel_id_list = hotel_ids.split(',')
        destination_id_list = destination_ids.split(',')

        for hotel in self.hotel_data:
            if hotel.id in hotel_id_list and str(hotel.destination_id) in destination_id_list:
                result.append(hotel)

        return result
