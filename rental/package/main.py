import admin_panel
import buyer_menu
import seller_menu
from file_operations import load_from_csv, load_from_json
from rent_service import RentService


def main():
    service = RentService()
    initial_data = load_from_csv("datapack.csv")

    for item in initial_data:
        service.add_stuff(item)
    # Load items from JSON and CSV
    items_from_json = load_from_json("datapack.json")
    items_from_csv = load_from_csv("datapack.csv")

    # Initialize RentService and add loaded items
    service = RentService()
    for item in items_from_json + items_from_csv:
        service.add_stuff(item)

    while True:
        print("\nWelcome to the Electronic devices Rent")
        print("1. Buyer Menu")
        print("2. Seller Menu")
        print("3. Admin Panel")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            buyer_menu.main(service)
        elif choice == "2":
            seller_menu.main(service)
        elif choice == "3":
            admin_panel.main(service)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
