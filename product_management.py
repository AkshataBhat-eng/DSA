import json
import os
import re

product_list = []
file_path = 'product_list.json'

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def displayProductInfo(self):
        print('Product Information')
        print('product name: ', self.name)
        print('product price: ', self.price)
        print('product quantity: ', self.quantity)

    def createProduct(self):
        print('Add new product')
        self.name = input('Enter the product name- ')
        self.price = int(input('Enter the product price- '))
        self.quantity = int(input('Enter the product quantity- '))
        
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r+') as file:
                try: 
                    product_list= json.load(file)
                except json.JSONDecodeError:
                    product_list = []
        else:
            product_list = []        
        product_list.append({
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        })
        with open(file_path, 'w') as file:
            json.dump(product_list, file)
        print('New product added')