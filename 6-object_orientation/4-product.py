class Product:

    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        print("Price setter called")
        if value<=0:
            raise ValueError("Price cannot be 0 or less")
        self.__price=value
    def get_price(self):
        print("Price getter called")
        return self.__price

    def __str__(self):
        return f"Product Name:{self.name} || Product Price: {self.__price}"

    price=property(get_price,set_price)

try:
    pr1=Product("Earphones",-300)
    pr1.price=-600
    print(pr1.price)
except ValueError as ex:
    print(ex)

pr2=Product("Keyboard",500)
print(pr2)