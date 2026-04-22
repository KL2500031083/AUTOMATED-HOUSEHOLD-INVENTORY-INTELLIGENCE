import csv
import json
from item import Item

def load_csv(file_name):
    items = {}
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, qty, expiry = row
                items[name] = Item(name, qty, expiry)
    except FileNotFoundError:
        pass
    return items


def save_csv(file_name, items):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for item in items.values():
            writer.writerow([item.name, item.quantity, item.expiry])


def save_json(file_name, items):
    data = [
        {"name": i.name, "quantity": i.quantity, "expiry": i.expiry}
        for i in items.values()
    ]
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


def load_json(file_name):
    items = {}
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            for i in data:
                items[i["name"]] = Item(i["name"], i["quantity"], i["expiry"])
    except:
        pass
    return items