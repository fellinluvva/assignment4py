import csv
import json
from datetime import datetime


class RentService:
    def __init__(self):
        self.stuff = []
        self.users = {}
        self.transactions = []

    def add_user(self, user_id, balance):
        self.users[user_id] = {'balance': balance, 'purchase_history': []}

    def add_stuff(self, good):
        self.stuff.append(good)

    def search_stuff(self, keyword):
        found_stuff = []
        for stuff in self.stuff:
            if keyword in stuff.name or keyword in stuff.description:
                found_stuff.append(stuff)
        return found_stuff

    def view_purchase_history(self, user_id):
        if user_id not in self.users:
            print("User ID not found.")
            return

        user_info = self.users[user_id]
        purchase_history = user_info['purchase_history']
        user_balance = user_info['balance']

        print(f"User: {user_id}")
        print(f"Balance: ${user_balance}")

        if purchase_history:
            print("Purchase history:")
            for item in purchase_history:
                print(f"{item.name} - ${item.price}")
        else:
            print("No purchase history.")

    def list_all_items(self):
        print("All items:")
        for item in self.stuff:
            print(f"{item.name} - ${item.price}")

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

        # Optionally, you can save the transactions to a file immediately
        self.save_transactions_to_json()
        self.save_transactions_to_csv()

    def save_transactions_to_json(self):
        with open("transactions.json", "w") as json_file:
            json.dump(self.transactions, json_file, indent=4)

    def save_transactions_to_csv(self):
        with open("transactions.csv", mode="w", newline="") as csv_file:
            fieldnames = ["timestamp", "buyer_id", "seller_id", "item_name", "price"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)

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

    def record_transaction(self, buyer_id, seller_id, item_name, price):
        pass  # You can implement this method to record the transaction details

    def update_user_json(self):
        with open("users.json", "w") as json_file:
            json.dump(self.users, json_file, indent=4)

    def update_user_csv(self):
        with open("users.csv", mode="w", newline="") as csv_file:
            fieldnames = ["user_id", "balance", "purchase_history"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for user_id, info in self.users.items():
                writer.writerow({
                    "user_id": user_id,
                    "balance": info["balance"],
                    "purchase_history": ', '.join(item.name for item in info["purchase_history"])
                })
