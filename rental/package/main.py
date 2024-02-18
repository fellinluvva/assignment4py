from rent_service import RentService
from file_operations import load_from_csv


def main():
    service = RentService()

    # Add users
    service.add_user("admin", 5000)
    service.add_user("user", 500)

    # Load data from csv
    initial_data = load_from_csv("datapack.csv")

    for item in initial_data:
        service.add_stuff(item)

    # Main menu loop for terminal
    while True:
        print("\nWelcome to the Electronic devices Rent")
        print("1. List all items")
        print("2. Search for items")
        print("3. Buy an item")
        print("4. View purchase history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.list_all_items()

        elif choice == "2":
            keyword = input("Enter a keyword to search for: ")
            found_stuff = service.search_stuff(keyword)
            if found_stuff:
                print("Found items:")
                for stuffs in found_stuff:
                    stuffs.display_info()
            else:
                print("Nothing found.")

        elif choice == "3":
            user_id = input("Enter your user_id: ")
            item_name = input("Enter the name of the item you want to buy: ")
            service.buy_item(user_id, item_name)

        elif choice == "4":
            user_id = input("Enter your username: ")
            service.view_purchase_history(user_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("404 error.")


if __name__ == "__main__":
    main()
