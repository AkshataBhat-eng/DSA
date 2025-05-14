import unittest
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

class shoppingCartUnitTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart('Amazon')
        self.product = Product('laptop', 40000, 2)
        self.product2 = Product('mobile', 30000, 2)
        self.product3 = Product('air-pods', 2000, 1)

    def test_func_1(self):
        self.cart.add_to_cart(self.product)
        self.assertEqual(len(self.cart.products), 1)

    def test_func_2(self):
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product)
        self.cart.remove_cart_item('mobile')
        self.assertEqual(len(self.cart.products), 1)
    
    def test_func_3(self):
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product)
        self.assertIn(self.product, self.cart.products)

    def test_func_4(self):
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product)
        self.assertNotIn(self.product3, self.cart.products)


        


if __name__ == "__main__":
    unittest.main()


    # p1 = Product('laptop', 40000, 2)
    # p1 = Product('laptop', 40000, 2)
    # p2 = Product('mobile', 20000, 1)
    # p3 = Product('charger', 2000, 1)

    # c1 = Cart('Akshata')
    # c1.add_to_cart(p1)
    # c1.add_to_cart(p2)
    # c1.add_to_cart(p3)

    # c1.display_cart()

    # c1.remove_cart_item('laptop')
    # print('******************')
    # c1.display_cart()
                
