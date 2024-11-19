import json
import argparse
import requests

from Acme import Acme 
from Paperflies import Paperflies 
from Patagonia import Patagonia 
from HotelsService import HotelsService


def fetch_hotels(hotel_ids, destination_ids):
    suppliers = [
        Acme(),
        Paperflies(),
        Patagonia(),
    ]

    # Fetch data from all suppliers
    all_supplier_data = []
    for supp in suppliers:
        all_supplier_data.extend(supp.fetch())

    # Merge all the data and save it in-memory somewhere
    svc = HotelsService()
    svc.merge_and_save(all_supplier_data)

    # # Fetch filtered data
    filtered = svc.find(hotel_ids, destination_ids)


    f = open("output.txt", "w")
    f.write(json.dumps(filtered, default=vars, indent=2))
    f.close()


    # # Return as json
    return json.dumps(filtered)
    

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("hotel_ids", type=str, help="Hotel IDs")
    parser.add_argument("destination_ids", type=str, help="Destination IDs")
    
    # Parse the arguments
    args = parser.parse_args()
    
    hotel_ids = args.hotel_ids
    destination_ids = args.destination_ids
    
    result = fetch_hotels(hotel_ids, destination_ids)
    # print(result)

if __name__ == "__main__":
    main()