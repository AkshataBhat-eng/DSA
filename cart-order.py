class CartItem:
    def __init__(self, product_id, name, price, quantity):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def addItems(self, product_id, name, price, quantity=1):
        # Get the new product details
        # check if the product is already present in the items list
        # if yes, update the quantity by adding the new quatity to it
        # if not, add the product to the items list

    def updateItem(self, product_id, quantity):
        # Get the new quantity and product id
        # check if the product_id is present in items list
        # if yes, update the quantity

    def removeItem(self, product_id):
        # get the product_id
        # check if the product is present in items list
        # if yes, remove that product from the list

    def clearCart(self):
        # remove all the items from the items list

    def calculateTotalprice(self):
        # calculate the sum of each item's price based on number of quatities available

class Order:
    def __init__(self, order_id, order_date, product_list, order_status, customer_name, customer_email, shipping_address):
        self.order_id = order_id
        self.order_date = order_date
        self.product_list = product_list
        self.order_status = order_status
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.shipping_address = shipping_address

class Ordermanager:
    def __init__(self):
        self.orders = {}

    def createOrder(self, order_id, products, customer_name, shipping_address):
        # get the details of the order and crate a new istace of Order class;
        # add the new order instance to the order_id index of orders list

    def getOrders(self, order_id):
        # return the order from orders list where id =order_id 

    def updateOrders(self, order_id, status):
        # get the order status and order_id
        # based on the order_id, updae the status of the order in the orders list

    def getOrdersByCustomer(self, customer_name, customer_email):
        # iterate through order list to 
        # check for each order customer_name and email
        # order for which these match, append it to customer_order list
        # return customer_order