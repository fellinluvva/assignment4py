class Stuff:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        pass


class Electronics(Stuff):
    def __init__(self, name, description, price, brand):
        super().__init__(name, description, price)
        self.brand = brand

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.brand} - ${self.price}")


class Furniture(Stuff):
    def __init__(self, name, description, price, material):
        super().__init__(name, description, price)
        self.material = material

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.material} - ${self.price}")
