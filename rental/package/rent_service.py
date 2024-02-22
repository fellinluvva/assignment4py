class RentService:
    def __init__(self):
        self.stuff = []
        self.users = {}

    # Add a user with a given user_id and initial balance
    def add_user(self, user_id, balance):
        self.users[user_id] = {'balance': balance, 'purchase_history': []}

    # Add a new item to the list of available stuff
    def add_stuff(self, good):
        self.stuff.append(good)

    # Search for stuff based on a keyword in the name or description, with optional sorting
    def search_stuff(self, keyword, sort_by=None):
        found_stuff = []
        for stuff in self.stuff:
            if keyword in stuff.name or keyword in stuff.description:
                found_stuff.append(stuff)

        if sort_by == "price":
            found_stuff.sort(key=lambda x: x.price)
        # Add more sorting options if needed

        return found_stuff

    # Buy an item for a specific user
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

        print("Purchase successful.")

    # View purchase history for a specific user
    def view_purchase_history(self, user_id):
        if user_id not in self.users:
            print("user_id not found.")
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

    # List all available items
    def list_all_items(self):
        print("All items:")
        for item in self.stuff:
            print(f"{item.name} - ${item.price}")

    # Edit item details
    def edit_item(self, item_name, new_description=None, new_price=None):
        for item in self.stuff:
            if item.name == item_name:
                if new_description:
                    item.description = new_description
                if new_price:
                    item.price = new_price
                print("Item details updated successfully.")
                return
        print("Item not found.")

    # Search for stuff within a price range
    def search_by_price_range(self, min_price, max_price):
        found_stuff = [stuff for stuff in self.stuff if min_price <= stuff.price <= max_price]
        return found_stuff

    # Track best-selling items
    def best_sellers(self, n=5):
        purchase_counts = {}
        for user_info in self.users.values():
            for item in user_info['purchase_history']:
                purchase_counts[item.name] = purchase_counts.get(item.name, 0) + 1

        sorted_items = sorted(purchase_counts.items(), key=lambda x: x[1], reverse=True)[:n]
        return sorted_items

    # Record buyers and sellers for each transaction
    def record_transaction(self, buyer_id, seller_id, item_name, price):
        if buyer_id not in self.users or seller_id not in self.users:
            print("Invalid buyer or seller.")
            return
        transaction_info = {'buyer': buyer_id, 'seller': seller_id, 'item': item_name, 'price': price}
        # Add transaction info to a database or file for future reference
        print("Transaction recorded successfully.")


