import csv
import json
from collections import defaultdict

def csv_to_json(csv_path, json_path=None):
    brand_dict = defaultdict(list)

    with open(csv_path, encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Format PRICE and COST to 2 decimal places
            row['PRICE'] = f"{float(row['PRICE']):.2f}"
            row['COST'] = f"{float(row['COST']):.2f}"
            brand = row.pop('BRAND')  # Remove BRAND from product details and use as key
            brand_dict[brand].append(row)

    # Convert defaultdict to regular dict for JSON serialization
    warehouse_dict = {"California": dict(brand_dict)}
    vendor_dict = {"Norcal Diesel Performance": dict(warehouse_dict)}

    if json_path:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(vendor_dict, json_file, indent=4)

    return vendor_dict

csv_path = 'test_data/norcal_inventory.csv'
json_path = 'test_data/norcal_inventory.json'
data = csv_to_json(csv_path, json_path)
