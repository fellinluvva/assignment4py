import csv
import json
from datetime import datetime


class RentService:
    def __init__(self):
        self.stuff = []  # Initialize list to store items
        self.users = {}  # Initialize dictionary to store users
        self.transactions = []  # Initialize list to store transactions

    # Method to add a new user
    def add_user(self, user_id, balance):
        self.users[user_id] = {'balance': balance, 'purchase_history': []}

    # Method to add a new item to the list of available items
    def add_stuff(self, good):
        self.stuff.append(good)

    # Method to search for items based on a keyword
    def search_stuff(self, keyword):
        found_stuff = []
        for stuff in self.stuff:
            if keyword in stuff.name or keyword in stuff.description:
                found_stuff.append(stuff)
        return found_stuff

    # Method to view purchase history for a user
    def view_purchase_history(self, user_id):
        if user_id not in self.users:
            print("User ID not found.")
            return

        user_info = self.users[user_id]
        user_balance = user_info['balance']

        print(f"User: {user_id}")
        print(f"Balance: ${user_balance}")

        # Load transaction data from JSON file
        with open("transactions.json", "r") as json_file:
            transactions = json.load(json_file)

        if transactions:
            print("Purchase history:")
            for transaction in transactions:
                if transaction["buyer_id"] == user_id:
                    print(f"Timestamp: {transaction['timestamp']}")
                    print(f"Item: {transaction['item_name']} - ${transaction['price']}")
        else:
            print("No purchase history.")

    # Method to list all available items
    def list_all_items(self):
        print("All items:")
        for item in self.stuff:
            print(f"{item.name} - ${item.price}")

    # Method to record a transaction
    def record_transaction(self, buyer_id, seller_id, item_name, price):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "timestamp": timestamp,
            "buyer_id": buyer_id,
            "seller_id": seller_id,
            "item_name": item_name,
            "price": price
        }
        self.transactions.append(transaction)

        # Save transactions to files
        self.save_transactions_to_json()
        self.save_transactions_to_csv()

    # Method to save transactions to JSON file
    def save_transactions_to_json(self):
        with open("transactions.json", "w") as json_file:
            json.dump(self.transactions, json_file, indent=4)

    # Method to save transactions to CSV file
    def save_transactions_to_csv(self):
        with open("transactions.csv", mode="w", newline="") as csv_file:
            fieldnames = ["timestamp", "buyer_id", "seller_id", "item_name", "price"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)

    # Method to handle item purchase
    def buy_item(self, buyer_id, item_name):
        if buyer_id not in self.users:
            print("Buyer ID not found.")
            return

        item = next((item for item in self.stuff if item.name == item_name), None)
        if not item:
            print("Item not found.")
            return

        buyer_info = self.users[buyer_id]
        if buyer_info['balance'] < item.price:
            print("Insufficient balance. Cannot complete purchase.")
            return

        # Update buyer's balance after a successful purchase
        buyer_info['balance'] -= item.price
        buyer_info['purchase_history'].append(item)

        # Find seller
        seller = next((user_id for user_id, info in self.users.items() if item in info['purchase_history']), None)
        if not seller:
            print("Seller not found.")
            return

        # Record transaction
        self.record_transaction(buyer_id, seller, item_name, item.price)

        # Update user JSON file
        self.update_user_json()

        # Update user CSV file
        self.update_user_csv()

        print("Purchase successful.")

    # Method to update user data in JSON format
    def update_user_json(self):
        users_copy = self.users.copy()
        for user_id, info in users_copy.items():
            purchase_history = []
            # Iterate through item names in purchase history
            for item_name in info['purchase_history']:
                # Find the corresponding item object from the list of stuff
                item = next((item for item in self.stuff if item.name == item_name), None)
                if item:
                    # If item is found, append its dictionary representation to purchase history
                    purchase_history.append(item.to_dict())
            # Update purchase history with the list of dictionaries
            info['purchase_history'] = purchase_history
        with open("users.json", "w") as json_file:
            json.dump(users_copy, json_file, indent=4)

    # Method to update user data in CSV format
    def update_user_csv(self):
        with open("users.csv", mode="w", newline="") as csv_file:
            fieldnames = ["user_id", "balance", "purchase_history"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for user_id, info in self.users.items():
                # Convert purchase history (list of items) into a list of item names
                purchase_history = [item.name for item in info["purchase_history"]]
                purchase_history_str = ', '.join(purchase_history)
                writer.writerow({
                    "user_id": user_id,
                    "balance": info["balance"],
                    "purchase_history": purchase_history_str
                })