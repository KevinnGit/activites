item_names = []          
item_prices = {}         

while True:
    print("\n----- INVENTORY MENU -----")
    print("1. Add New Item")
    print("2. Update Item Price")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ADD NEW ITEM
    if choice == "1":
        try:
            count = int(input("How many items do you want to add? "))
            if count <= 0:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid number! Enter a whole number only.")
            continue

        for i in range(count):
            print(f"\nAdding item {i+1} of {count}")

            name = input("Enter item name: ").strip()

            # check duplicate
            if name in item_names:
                print("Error: Item already exists! Skipping...")
                continue

            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("Invalid price! Skipping this item.")
                continue

            # Add to list and dictionary 
            item_names.append(name)
            item_prices[name] = price
            print(f"Item '{name}' added successfully!")

    # UPDATE PRICE
    elif choice == "2":
        name = input("Enter item name to update: ").strip()

        if name not in item_names:
            print("Error: Item not found!")
        else:
            try:
                new_price = float(input("Enter new price: "))
                item_prices[name] = new_price
                print(f"Price of '{name}' updated to {new_price}")
            except ValueError:
                print("Invalid price! Please enter numbers only.")

    # VIEW INVENTORY
    elif choice == "3":
        print("\n--- CURRENT INVENTORY ---")
        if len(item_names) == 0:
            print("Inventory is empty.")
        else:
            for item in item_names:
                print(f"{item} : ₱{item_prices[item]}")

    # EXIT
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
