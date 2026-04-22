from inventory import Inventory
from alerts import low_stock_alert, expiry_alert
from analytics import show_analysis

def main():
    inv = Inventory()

    while True:
        print("\n==== HI-CAS MENU ====")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Low Stock Alert")
        print("6. Expiry Alert")
        print("7. Analytics")
        print("8. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            name = input("Name: ")
            qty = input("Quantity: ")
            exp = input("Expiry (YYYY-MM-DD): ")
            inv.add_item(name, qty, exp)

        elif ch == "2":
            name = input("Name: ")
            qty = input("New Quantity: ")
            inv.update_item(name, qty)

        elif ch == "3":
            name = input("Name: ")
            inv.delete_item(name)

        elif ch == "4":
            inv.display_items()

        elif ch == "5":
            low_stock_alert(inv.items)

        elif ch == "6":
            expiry_alert(inv.items)

        elif ch == "7":
            show_analysis(inv.items)

        elif ch == "8":
            inv.save()
            print("Saved & Exit")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()