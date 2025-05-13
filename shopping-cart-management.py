class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self, username):
        self.username = ''
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def remove_cart_item(self, name):
        for prod in self.products:
            if prod.name == name:
                self.products.remove(prod)

    def display_cart(self):
        for prod in self.products:
            print('name: ',prod.name,' price: ',prod.price, 'quantity: ',prod.quantity )
            print('------------------------------------------------------------------------------')


p1 = Product('laptop', 40000, 2)
p1 = Product('laptop', 40000, 2)
p2 = Product('mobile', 20000, 1)
p3 = Product('charger', 2000, 1)

c1 = Cart('Akshata')
c1.add_to_cart(p1)
c1.add_to_cart(p2)
c1.add_to_cart(p3)

c1.display_cart()

c1.remove_cart_item('laptop')
print('******************')
c1.display_cart()
                
