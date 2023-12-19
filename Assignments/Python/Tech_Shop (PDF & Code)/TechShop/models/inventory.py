from models.products import Products
from db_connector.db_connector import get_db_connection
class Inventory:
    def __init__(self, inventory_id, product: Products, quantity_in_stock, last_stock_update):
        self.connection = get_db_connection()
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    # Getter for inventory_id
    def get_inventory_id(self):
        return self.__inventory_id

    # Getter for product
    def get_product(self):
        return self.__product

    # Setter for product
    def set_product(self, product:Products):
        cursor = self.connection.cursor()
        sql = 'UPDATE inventory SET ProductID = %s WHERE inventoryID = %s'
        para = (product.get_product_id(), self.__inventory_id)
        cursor.execute(sql, para)
        self.__product = product

    # Getter for quantity_in_stock
    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    # Setter for quantity_in_stock
    def set_quantity_in_stock(self, quantity_in_stock):
        cursor = self.connection.cursor()
        sql = 'UPDATE inventory SET QuantityInStock = %s WHERE inventoryID = %s'
        para = (quantity_in_stock, self.__inventory_id)
        cursor.execute(sql, para)
        self.__quantity_in_stock = quantity_in_stock

    # Getter for last_stock_update
    def get_last_stock_update(self):
        return self.__last_stock_update

    # Setter for last_stock_update
    def set_last_stock_update(self, last_stock_update):
        cursor = self.connection.cursor()
        sql = 'UPDATE inventory SET LastStockUpdate = %s WHERE inventoryID = %s'
        para = (last_stock_update, self.__inventory_id)
        cursor.execute(sql, para)
        self.__last_stock_update = last_stock_update

    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def add_to_inventory(self, quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE inventory SET QuantityInStock = %s WHERE inventoryID = %s'
        para = (self.__quantity_in_stock + quantity, self.__inventory_id)
        cursor.execute(sql, para)
        self.__quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        if self.__quantity_in_stock >= quantity:
            cursor = self.connection.cursor()
            sql = 'UPDATE inventory SET QuantityInStock = %s WHERE inventoryID = %s'
            para = (self.__quantity_in_stock - quantity, self.__inventory_id)
            cursor.execute(sql, para)
            self.__quantity_in_stock -= quantity
        else:
            print("Error: Insufficient quantity in stock.")
            return

    def update_stock_quantity(self, new_quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE inventory SET QuantityInStock = %s WHERE inventoryID = %s'
        para = (new_quantity, self.__inventory_id)
        cursor.execute(sql, para)
        self.__quantity_in_stock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.__quantity_in_stock * self.__product.get_price()

    def list_low_stock_products(self, threshold):
        if self.__quantity_in_stock < threshold:
            return f"{self.__product.get_product_name()} is below the threshold with {self.__quantity_in_stock} units."

    def list_out_of_stock_products(self):
        if self.__quantity_in_stock == 0:
            return f"{self.__product.get_product_name()} is out of stock."
        else:
            return f"No product is out of stock"

    def list_all_products(self):
        return f"Product: {self.__product.get_product_details()}, Quantity in Stock: {self.__quantity_in_stock}"
