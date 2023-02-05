from Product import Product


class InventoryError(Exception):
    pass


class Inventory:

    def __init__(self):
        self.list = []
        self.list_of_prod: list[Product] = []

    def __repr__(self):
        ret = ''
        for item in self.list:
            ret += str(self.get_by_id(item))
        return ret

    def get_by_id(self, num):
        if num in self.list:
            return self.list_of_prod[self.list.index(num)]
        else:
            raise InventoryError("Out of Inventory")

    def add_prod(self, product: Product):
        if product.ID in self.list:
            if self.list_of_prod[self.list.index(product.ID)].Price == product.Price:
                self.list_of_prod[self.list.index(product.ID)].Quantity += product.Quantity
            else:
                print("Prices are different")
        if product.Quantity:
            self.list_of_prod.append(product)
            self.list.append(product.ID)

    def rm_product(self, product: Product):
        self.list.pop(self.list_of_prod.index(product))
        self.list_of_prod.remove(product)

    def sum_of_products(self, dollar=False):
        """returns the quantity left in inventory, if dollar flag is True, returns $$$"""
        quantity = 0
        cash = 0
        for item in self.list_of_prod:
            quantity += item.Quantity
            cash += item.Quantity * item.Price
        if dollar:
            return cash
        return quantity


