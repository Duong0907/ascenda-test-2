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
                # all_supplier_data.pop(i)
            else:
                self.hotel_data.append(curr)
                curr = all_supplier_data[i]

            i += 1

        if curr not in self.hotel_data:
            self.hotel_data.append(curr)


        # self.hotel_data = all_supplier_data

    def find(self, hotel_ids, destination_ids):
        return self.hotel_data
