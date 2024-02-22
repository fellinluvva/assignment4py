from rent_service import RentService
from file_operations import *
from rental.package.stuff import Furniture, Electronics


def main():
    service = RentService()

    users_data_csv = load_users_from_csv("users.csv")
    service.users = users_data_csv

    # Load data from csv
    initial_data = load_from_csv("datapack.csv")

    for item in initial_data:
        service.add_stuff(item)

    # Main menu loop for terminal
    while True:
        print("\nWelcome to the Electronic devices Rent")
        print("1. Buyer Menu")
        print("2. Seller Menu")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            buyer_menu(service)
        elif choice == "2":
            seller_menu(service)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def buyer_menu(service):
    while True:
        print("\nBuyer Menu:")
        print("1. List all items")
        print("2. Search for items")
        print("3. Buy an item")
        print("4. View purchase history")
        print("5. Exit Buyer Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.list_all_items()
        elif choice == "2":
            keyword = input("Enter a keyword to search for: ")
            found_stuff = service.search_stuff(keyword)
            if found_stuff:
                print("Found items:")
                for stuff in found_stuff:
                    stuff.display_info()
            else:
                print("Nothing found.")
        elif choice == "3":
            user_id = input("Enter your user ID: ")
            item_name = input("Enter the name of the item you want to buy: ")
            service.buy_item(user_id, item_name)
        elif choice == "4":
            user_id = input("Enter your user ID: ")
            service.view_purchase_history(user_id)
        elif choice == "5":
            print("Exiting Buyer Menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def seller_menu(service):
    while True:
        print("\nSeller Menu:")
        print("1. View sales report")
        print("2. Add new item")
        print("3. Exit Seller Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of top sellers you want to see: "))
            top_sellers = service.best_sellers(n)
            if top_sellers:
                print("Top sellers:")
                for item, count in top_sellers:
                    print(f"{item} - Sold: {count}")
            else:
                print("No sales data available.")
        elif choice == "2":
            add_new_item(service)
        elif choice == "3":
            print("Exiting Seller Menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def add_new_item(service):
    type_ = input("Enter type (Electronics/Furniture): ")
    name = input("Enter name: ")
    description = input("Enter description: ")
    price = float(input("Enter price: "))
    if type_.lower() == "electronics":
        brand = input("Enter brand: ")
        new_item = Electronics(name, description, price, brand)
    elif type_.lower() == "furniture":
        material = input("Enter material: ")
        new_item = Furniture(name, description, price, material)
    else:
        print("Invalid item type.")
        return

    service.add_stuff(new_item)
    print("Item added successfully.")

    # Update JSON file
    existing_data = load_from_json("datapack.json")  # Load existing data
    existing_data.append(new_item)  # Append the new item instance
    save_to_json(existing_data, "datapack.json")  # Save data to JSON file

    # Update CSV file
    save_to_csv(existing_data, "datapack.csv")  # Save data to CSV file


if __name__ == "__main__":
    main()
