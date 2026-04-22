from file_handler import load_csv, save_csv

class Inventory:
    def __init__(self, file_name="inventory.csv"):
        self.file_name = file_name
        self.items = load_csv(file_name)

    # CREATE
    def add_item(self, name, quantity, expiry):
        self.items[name] = self.items.get(name) or None
        from item import Item
        self.items[name] = Item(name, quantity, expiry)
        print("Item added!")

    # UPDATE
    def update_item(self, name, quantity):
        if name in self.items:
            self.items[name].quantity = int(quantity)
            print("Item updated!")
        else:
            print("Item not found!")

    # DELETE
    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            print("Item deleted!")
        else:
            print("Item not found!")

    # READ
    def display_items(self):
        if not self.items:
            print("Inventory empty")
            return
        for item in self.items.values():
            print(item)

    def save(self):
        save_csv(self.file_name, self.items)