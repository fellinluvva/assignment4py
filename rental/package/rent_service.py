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

    # Search for stuff based on a keyword in the name or description
    def search_stuff(self, keyword):
        found_stuff = []
        for stuffs in self.stuff:
            if keyword in stuffs.name or keyword in stuffs.description:
                found_stuff.append(stuffs)
        return found_stuff

    # Buy an item for a specific user
    def buy_item(self, user_id, item_name):
        if user_id not in self.users:
            print("user_id not found.")
            print("Current users:", self.users)  # Print users for ease in debug
            return

        item = next((item for item in self.stuff if item.name == item_name), None)
        if not item:
            print("Item not found.")
            return

        if self.users[user_id]['balance'] < item.price:
            print("Insufficient balance. Cannot complete purchase.")
            return

        # Decrease user's balance after a successful purchase
        self.users[user_id]['balance'] -= item.price
        self.users[user_id]['purchase_history'].append(item)
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