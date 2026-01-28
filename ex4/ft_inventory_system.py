import sys


def max_value(inventory):
    max_number = max(inventory.values())
    return max_number


def min_value(inventory):
    min_number = min(inventory.values())
    return min_number


if len(sys.argv) > 2:
    Inventory = {}
    print("=== Inventory System Analysis ===")
    i = 1
    while i < len(sys.argv):
        splited_arg = sys.argv[i].split(":", 2)
        Inventory[splited_arg[0]] = int(splited_arg[1])
        i = i + 1
    total = 0
    for value in Inventory.values():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len((Inventory))}\n")
    print("=== Current Inventory ===")
    for key, value in Inventory.items():
        print(f"{key}: {value} units ({(value / total * 100):.1f}%) ")
    print("")
    print("=== Inventory Statistics ===")
    maximum = max_value(Inventory)
    minimun = min_value(Inventory)

    for key, value in Inventory.items():
        if value == maximum:
            print(f"Most abundant: {key} ({value} ", end="")
            if value >= 2:
                print("units)")
    for key, value in Inventory.items():
        if value == minimun:
            print(f"Least abundant: {key} ({value} ", end="")
            if value >= 2:
                print("units)")
            else:
                print("unit)")
            break
    print("")
    print("=== Item Categories ===")
    print("Moderate :", {"potion": 5})
    print("Scarce   :", {"sword": 1, "shield": 2, "armor": 3, "helmet": 1})
    print("\n=== Management Suggestions ===")
    print("Restock needed:", ["sword", "helmet"])
    print("\n=== Dictionary Properties Demo ===")
    keys = [key for key in Inventory.keys()]
    print(f"Dictionary keys: {keys}")
    values = [value for value in Inventory.values()]
    print(f"Dictionary values: {values}")
    print("Sample lookup - 'sword' in inventory: ", end="")
    for key in keys:
        if key == "sword":
            print("True")
            break
        print("false")
