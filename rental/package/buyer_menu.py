
def list_of_items(service):
    service.list_all_items()


def search_items(service):
    keyword = input("Enter a keyword to search for: ")
    found_stuff = service.search_stuff(keyword)
    if found_stuff:
        print("Found items:")
        for stuffs in found_stuff:
            stuffs.display_info()
    else:
        print("Nothing found.")


def buy_item(service):
    user_id = input("Enter your user_id: ")
    item_name = input("Enter the name of the item you want to buy: ")
    service.buy_item(user_id, item_name)


def view_purchase_history(service):
    user_id = input("Enter your username: ")
    service.view_purchase_history(user_id)


def main(service):
    while True:
        print("\nBuyer Menu:")
        print("1. List all items")
        print("2. Search for items")
        print("3. Buy an item")
        print("4. View purchase history")
        print("5. Exit Buyer Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_of_items(service)
        elif choice == "2":
            search_items(service)
        elif choice == "3":
            buy_item(service)
        elif choice == "4":
            view_purchase_history(service)
        elif choice == "5":
            print("Exiting Buyer Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
