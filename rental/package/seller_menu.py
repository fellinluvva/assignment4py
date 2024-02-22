from rental.package.file_operations import load_from_json, save_to_json, save_to_csv
from rental.package.stuff import Electronics, Furniture


def view_sales_report(service):
    n = int(input("Enter the number of top sellers you want to see: "))
    top_sellers = service.best_sellers(n)
    if top_sellers:
        print("Top sellers:")
        for item, count in top_sellers:
            print(f"{item} - Sold: {count}")
    else:
        print("No sales data available.")


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


def main(service):
    while True:
        print("\nSeller Menu:")
        print("1. View sales report")
        print("2. Add new item")
        print("3. Exit Seller Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_sales_report(service)
        elif choice == "2":
            add_new_item(service)
        elif choice == "3":
            print("Exiting Seller Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
