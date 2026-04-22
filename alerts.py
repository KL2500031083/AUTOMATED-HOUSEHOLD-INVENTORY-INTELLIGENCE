def low_stock_alert(items, threshold=2):
    print("\nLow Stock Items:")
    for item in items.values():
        if item.quantity <= threshold:
            print(item)


def expiry_alert(items):
    print("\nExpired / Expiring Items:")
    for item in items.values():
        if item.is_expired():
            print(item)