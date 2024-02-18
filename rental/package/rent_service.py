class RentService:
    def __init__(self):
        self.stuff = []
        self.users = {}

    def add_user(self, user_id, balance):
        self.users[user_id] = {'balance': balance, 'purchase_history': []}

    def add_stuff(self, good):
        self.stuff.append(good)

    def search_stuff(self, keyword):
        found_stuff = []
        for stuffs in self.stuff:
            if keyword in stuffs.name or keyword in stuffs.description:
                found_stuff.append(stuffs)
        return found_stuff

    def buy_item(self, user_id, item_name):
        if user_id not in self.users:
            print("user_id not found.")
            print("Current users:", self.users)  # Print users for debugging
            return

        item = next((item for item in self.stuff if item.name == item_name), None)
        if not item:
            print("Item not found.")
            return

        if self.users[user_id]['balance'] < item.price:
            print("Insufficient balance. Cannot complete purchase.")
            return

        self.users[user_id]['balance'] -= item.price
        self.users[user_id]['purchase_history'].append(item)
        print("Purchase successful.")

    def view_purchase_history(self, user_id):
        if user_id not in self.users:
            print("user_id not found.")
            return

        purchase_history = self.users[user_id]['purchase_history']
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
