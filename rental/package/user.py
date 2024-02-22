class User:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

    def __str__(self):
        return f"User ID: {self.user_id}, Balance: {self.balance}"