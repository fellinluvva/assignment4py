import csv
import json
from stuff import *


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'name', 'description', 'price', 'brand', 'material']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item.to_dict())


def load_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'Electronics':
                data.append(Electronics(row['name'], row['description'], float(row['price']), row['brand']))
            elif row['type'] == 'Furniture':
                data.append(Furniture(row['name'], row['description'], float(row['price']), row['material']))
    return data


def save_to_json(data, filename):
    serialized_data = []
    for item in data:
        serialized_data.append(item.to_dict())

    with open(filename, 'w') as jsonfile:
        json.dump(serialized_data, jsonfile, indent=4)


def load_from_json(filename):
    data = []
    with open(filename) as jsonfile:
        serialized_data = json.load(jsonfile)
        for item_data in serialized_data:
            if item_data['type'] == 'Electronics':
                data.append(Electronics(item_data['name'], item_data['description'], item_data['price'], item_data['brand']))
            elif item_data['type'] == 'Furniture':
                data.append(Furniture(item_data['name'], item_data['description'], item_data['price'], item_data['material']))
    return data





