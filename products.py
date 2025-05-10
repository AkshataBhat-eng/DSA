class Product:
    def __init__(self, product_id, name, description, price, images, category, brand, composition, prescription_required):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.images = images  #List of image URLs or file paths
        self.category = category #such as "pain-relief, cold, fever"
        self.brand = brand
        self.composition = composition  #List of ingredients
        self.prescription_required = prescription_required
        self.variants = {}  #Dictionary to hold variants with variant_id as key

    def add_variant(self, variant_id, dosage, packaging, price, stock):
        # Helps to add a variant to the given product
        # variant inludes variant_id, dosage, packaging, price and stock

class ProductCatalog:
    def __init__(self):
        self.products = {}  #Dictionary to hold products with product_id as key

    def add_product(self, product):
        # Helps to add new products to products dictionary

    def get_products(self):
        #  Helps to get all the products

    def get_product_by_id(self, product_id):
        # Helps to get the products based on product_id

    def get_products_by_category(self, category):
        # Helps to get the products based on the category

    def search_by_filters(self, category=None, brand=None, price_range=None, composition=None):
        # Helps to get the products list based on filters
        # get the filter- category|brand|price_range|composition
        # use it as parameter to filter the products dictionary
        # return the list

class InventoryManager:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def add_product_to_inventory(self, product_id, variant_id, dosage, packaging, price, stock):
        # Helps to add product variants to the product present in inventory
        # check if the product_id is present in the product_catalog
        # if present, add the variant using the given information like dosage, packaging, price and stock
        # if not return response message: Product not found! 
        
    def update_product_quantity(self, product_id, variant_id, quantity):
        # Helps to update the product quantity when a product is added or removed from he inventory
        # check if the product_id is present in the product_catalog
        # if present and if product's variant_id is in the product, update the stock with the given quantity
        # if not, return response message Product or variant not found.

    def check_low_stock(self, threshold, product_id):
        # Returns if the product's stock is less than the threshold.
        # get the product_id
        # if product_id is present in the catalog, then compare the product stock against the given threshold
        # if stock is less than threshold return true
        # else return false