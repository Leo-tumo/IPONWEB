class ProductError(Exception):
    pass


class Product:

    def __init__(self, price, id, quantity):
        self.Price = price
        self.ID = id
        self.Quantity = quantity


    @property
    def Price(self):
        return self.__price

    @Price.setter
    def Price(self, value):
        if type(value) != int:
            raise ProductError(f"must be int not {type(value)}")
        if value < 0:
            raise ProductError("Must be positive")
        self.__price = value

    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, value):
        if type(value) != int:
            raise ProductError(f"must be int not {type(value)}")
        if value < 0:
            raise ProductError("Must be positive")
        self.__id = value

    @property
    def Quantity(self):
        return self.__quantity

    @Quantity.setter
    def Quantity(self, value):
        if type(value) != int:
            raise ProductError(f"must be int not {type(value)}")
        if value < 0:
            raise ProductError("Must be positive")
        self.__quantity = value

    def __repr__(self):
        return f'ID:{self.ID} ${self.Price} left:{self.Quantity}'

    def buy(self, count):
        if count > self.Quantity:
            raise ProductError(f"Sorry, only left {self.Quantity} items")
        self.Quantity -= count
















