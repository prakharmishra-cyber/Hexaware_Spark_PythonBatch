from datetime import datetime
from db_connector.db_connector import get_db_connection
from models.customers import Customers
from models.orders import Orders
from models.products import Products

class OrderDetails:
    def __init__(self, order_detail_id, order: Orders, product: Products, quantity):
        self.connection = get_db_connection()
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    # Getter for order_detail_id
    def get_order_detail_id(self):
        return self.__order_detail_id

    # Getter for order
    def get_order(self):
        return self.__order

    # Getter for product
    def get_product(self):
        return self.__product

    # Setter for product
    def set_product(self, product: Products):
        cursor = self.connection.cursor()
        sql = 'UPDATE orderdetails SET ProductID = %s WHERE OrderDetailID = %s'
        para = (product.get_product_id(), self.__order_detail_id)
        cursor.execute(sql, para)
        self.__product = product

    # Getter for quantity
    def get_quantity(self):
        return self.__quantity

    # Setter for quantity
    def set_quantity(self, quantity):
        if quantity < 0:
            print('Enter a valid quantity')
            return
        cursor = self.connection.cursor()
        sql = 'UPDATE orderdetails SET Quantity = %s WHERE OrderDetailID = %s'
        para = (quantity, self.__order_detail_id)
        cursor.execute(sql, para)
        self.__quantity = quantity

    def calculate_subtotal(self):
        return self.__product.get_price() * self.__quantity

    def get_order_detail_info(self):
        details = f"Order Detail ID: {self.__order_detail_id}\n"
        details += f"Order: {self.__order.get_order_details()}\n"
        details += f"Product: {self.__product.get_product_details()}\n"
        details += f"Quantity: {self.__quantity}\n"
        details += f"Subtotal: ${self.calculate_subtotal():.2f}\n"
        return details

    def update_quantity(self, new_quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE orderdetails SET Quantity = %s WHERE OrderDetailID = %s'
        para = (new_quantity, self.__order_detail_id)
        cursor.execute(sql, para)
        self.__quantity = new_quantity

    def add_discount(self, discount_percentage):
        discount_factor = 1 - (discount_percentage / 100)
        subtotal = self.calculate_subtotal()
        discounted_subtotal = subtotal * discount_factor
        print(f'Discounted Subtotal {discounted_subtotal}')

