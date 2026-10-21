# ==========================================================
# Title: Inventory List Analyzer - Store Stock Tracker
# Total Marks: 70
# Student ID: 061096
# Topics: Control, String Handling, Collection, Array, Built-in, Sorting
# ==========================================================

def main():
    print("Welcome to Inventory List Analyzer!")
    print("-" * 40)

    # 1. CONTROL STRUCTURE & LOOPING
    # Using list of tuples to store records -> [("milk", "dairy", 20), ...]
    inventory = []

    while True:
        # 2. STRING HANDLING - strip whitespace, lower for logic
        item_name = input("\nEnter item name: ").strip()
        while item_name == "":
            print("! Name cannot be empty")
            item_name = input("Enter item name: ").strip()

        category = input("Enter category: ").strip()
        while category == "":
            print("! Category cannot be empty")
            category = input("Enter category: ").strip()

        # Validate quantity with loop
        while True:
            try:
                qty = int(input("Enter quantity: ").strip())
                if qty < 0:
                    print("! Quantity cannot be negative")
                    continue
                break
            except ValueError:
                print("! Please enter a valid number")

        # Store as tuple (requirement 3)
        # Original case saved, but logic uses lower
        inventory.append((item_name, category, qty))

        # Ask to continue - looping condition
        choice = input("\nDo you want to add more items? (y/n): ").strip().lower()
        if choice != 'y':
            break

    if len(inventory) == 0:
        print("No data entered!")
        return

    # 2. STRING HANDLING - Search with substring logic
    print("\n--- String Handling ---")
    search_term = "ri"  # example substring search
    print(f"Searching items containing '{search_term}':")
    for name, cat, q in inventory:
        if search_term.lower() in name.lower(): # substring logic
            print(f"  Found: {name} in {cat}")

    # 3. COLLECTION DATATYPES
    # a) Dictionary -> item name to quantity
    item_dict = {}
    for name, cat, qty in inventory:
        key = name.lower() # convert to lowercase for dictionary key
        item_dict[key] = item_dict.get(key, 0) + qty
    
    print("\n--- Collection Datatypes ---")
    print(f"Dictionary (item -> quantity): {item_dict}")

    # b) List of tuples (already made)
    print(f"List of tuples: {inventory}")

    # c) Set -> unique categories
    category_set = set([cat.lower().strip() for name, cat, qty in inventory])
    print(f"Unique Categories (Set): {category_set}")

    # 4. ARRAY (LIST) USAGE - total, average, min, max
    quantities = [qty for name, cat, qty in inventory]
    
    # 5. BUILT-IN FUNCTIONS
    total = sum(quantities)
    avg = total / len(quantities)
    maximum = max(quantities)
    minimum = min(quantities)
    count = len(quantities)

    print("\n--- Array & Built-in Functions Analysis ---")
    print(f"Total Quantity in Stock: {total}")
    print(f"Average Quantity: {avg:.2f}")
    print(f"Max Quantity: {maximum}")
    print(f"Min Quantity: {minimum}")
    print(f"Total Records: {count}")

    # Find which item has max/min
    for name, cat, qty in inventory:
        if qty == maximum:
            print(f"Most Stocked Item: {name.title()} ({qty} units)")
        if qty == minimum:
            print(f"Least Stocked Item: {name.title()} ({qty} units)")

    # 6. SORTING
    print("\n--- Sorting ---")
    # a) Sort by quantity descending
    sorted_by_qty = sorted(inventory, key=lambda x: x[2], reverse=True)
    print("Items Sorted by Quantity (High to Low):")
    for i, (name, cat, qty) in enumerate(sorted_by_qty, 1):
        print(f"  {i}. {name.title()} - {qty} units")

    # b) Sort categories alphabetically
    sorted_categories = sorted(category_set)
    print("\nCategories Sorted Alphabetically:")
    for i, cat in enumerate(sorted_categories, 1):
        print(f"  {i}. {cat}")

    print("\n" + "="*40)
    print("END OF REPORT")
    print("="*40)

if __name__ == "__main__":
    main()