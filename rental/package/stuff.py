class Stuff:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    # Method to display information about the item
    def display_info(self):
        pass

    # Method to convert the item to a dictionary
    def to_dict(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Electronics(Stuff):
    def __init__(self, name, description, price, brand):
        super().__init__(name, description, price)
        self.brand = brand

    # Method to display information about the electronics item
    def display_info(self):
        print(f"{self.name} - {self.description} - {self.brand} - ${self.price}")

    # Method to convert the electronics item to a dictionary
    def to_dict(self):
        return {
            'type': type(self).__name__,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'brand': self.brand
        }


class Furniture(Stuff):
    def __init__(self, name, description, price, material):
        super().__init__(name, description, price)
        self.material = material

    # Method to display information about the furniture item
    def display_info(self):
        print(f"{self.name} - {self.description} - {self.material} - ${self.price}")

    # Method to convert the furniture item to a dictionary
    def to_dict(self):
        return {
            'type': type(self).__name__,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'material': self.material
        }