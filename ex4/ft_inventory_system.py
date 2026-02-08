import sys


def max_item(inventory: dict[dict[str: int]]):
    max_qty = max(item["quantity"] for item in inventory.values())
    for name, data in inventory.items():
        if data["quantity"] == max_qty:
            return name, max_qty


def min_item(inventory):
    min_qty = min(item["quantity"] for item in inventory.values())
    for name, data in inventory.items():
        if data["quantity"] == min_qty:
            return name, min_qty


def categorie_items(Inventory):
    categorie = {"Abundant": {}, "Moderate": {}, "Scarce": {}}
    for key, value in Inventory.items():
        if value["quantity"] >= 10:
            categorie["Abundant"].update({key: value["quantity"]})
        elif value["quantity"] >= 5:
            categorie["Moderate"].update({key: value["quantity"]})
        else:
            categorie["Scarce"].update({key: value["quantity"]})
    return categorie


def restrock_needed(Inventory):
    restrock = []
    for key, value in Inventory.items():
        if value["quantity"] <= 1:
            restrock += [key]
    return restrock


def get_key(Inventory_items):
    return Inventory_items[1]["quantity"]


if len(sys.argv) > 2:
    Inventory = {}
    print("=== Inventory System Analysis ===")
    for arg in sys.argv[1:]:
        try:
            name, qty = arg.split(":")
            qty = int(qty)
            Inventory.update({name: {"quantity": qty}})
        except ValueError:
            continue
    total = sum(item["quantity"] for item in Inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len((Inventory))}\n")
    print("=== Current Inventory ===")
    for item, value in sorted(Inventory.items(), key=get_key, reverse=True):
        # Understand how the sorted work + how the functio not have a
        # parameter and works
        qty = value["quantity"]
        print(f"{item}: {qty} unites ({(qty / total * 100):.1f}%)")
    print("")
    print("=== Inventory Statistics ===")
    name_max, max = max_item(Inventory)
    name_min, min = min_item(Inventory)
    print(f"Most abundant: {name_max} ({max} units)")
    print(f"Least abundant: {name_min} ({min} units)")
    print()
    print("=== Item Categories ===")
    categorie = categorie_items(Inventory)
    for key, value in categorie.items():
        if value:
            print(f"{key}: {value}")
    print("\n=== Management Suggestions ===")
    restrock = restrock_needed(Inventory)
    print(f"Restock needed: {restrock}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(Inventory.keys())}")
    values = []
    for value in Inventory.values():
        values += [value["quantity"]]
    print(f"Dictionary values: {values}")
    check_item = "sword"
    print(f"Sample lookup - '{check_item}' "
          f"in inventory: {check_item in Inventory}")
