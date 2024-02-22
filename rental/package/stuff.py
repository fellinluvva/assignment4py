class Stuff:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        pass

    def to_dict(self):
        return {
            'type': type(self).__name__,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

class Electronics(Stuff):
    def __init__(self, name, description, price, brand):
        super().__init__(name, description, price)
        self.brand = brand

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.brand} - ${self.price}")

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict['brand'] = self.brand
        return base_dict


class Furniture(Stuff):
    def __init__(self, name, description, price, material):
        super().__init__(name, description, price)
        self.material = material

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.material} - ${self.price}")

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict['material'] = self.material
        return base_dict