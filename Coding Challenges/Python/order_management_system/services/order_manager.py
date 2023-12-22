from datetime import date

from db_connector.db_adapter import *
from models.orders import Order
from models.product import Product
from models.user import User
from custom_exception.custome_exceptions import *


class OrderManager:

    def __init__(self):
        self.connection = get_db_connection()

    def get_all_products(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Product
            '''
            my_cursor.execute(sql)
            x = [Product(*list(i)) for i in list(my_cursor.fetchall())]
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_order_by_user(self, user_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * FROM Orders WHERE userID = %s
            '''
            para = (user_id,)
            my_cursor.execute(sql, para)
            x = [Order(*list(i)) for i in list(my_cursor.fetchall())]
            return x
        except Exception as e:
            print(f'An error occurred: {e}')

    def create_user(self, user_id, user_name, password, role):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                INSERT INTO User(userId, username, password, role)
                VALUES(%s, %s, %s, %s)
            '''
            para = (user_id, user_name, password, role)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('User Created successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def create_product(self, user, product_name, description, price, quantity_in_stock, product_type):
        try:
            my_cursor = self.connection.cursor()
            if user.get_user_role() != 'Admin':
                print('Product creation not permitted (Not admin)')
                return
            sql = '''
                    INSERT INTO Product(productId, productName, description, price, quantityInStock, type)
                    VALUES(%s, %s, %s, %s, %s, %s)
                        '''
            para = (get_ids('product', 'productId'), product_name, description, price, quantity_in_stock, product_type)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Product Created successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def user_exists(self, user_id):
        my_cursor = self.connection.cursor()
        sql = '''
        select count(*) from user where userId = %s
        '''
        para = (user_id,)
        my_cursor.execute(sql, para)
        x = int(my_cursor.fetchone()[0])
        return x != 0

    def order_exists(self, order_id):
        my_cursor = self.connection.cursor()
        sql = '''
        select count(*) from Orders where order_id = %s
        '''
        para = (order_id,)
        my_cursor.execute(sql, para)
        x = int(my_cursor.fetchone()[0])
        return x != 0

    def get_user_by_id(self, user_id):
        try:
            if not self.user_exists(user_id):
                raise UserNotFound('The specified user does not exist')
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM User WHERE userId = %s
            '''
            para = (user_id,)
            my_cursor.execute(sql, para)
            x = list(my_cursor.fetchone())
            return User(*x)
        except UserNotFound as e:
            print(f'User Not Found: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_order_by_id(self, order_id):
        try:
            if not self.order_exists(order_id):
                raise OrderNotFound('The specified order does not exist')
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Orders WHERE order_id = %s
            '''
            para = (order_id,)
            my_cursor.execute(sql, para)
            x = list(my_cursor.fetchone())
            return Order(*x)
        except OrderNotFound as e:
            print(f'Order Not Found: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def create_order(self, user_id, product, shipping_address):
        try:
            my_cursor = self.connection.cursor()
            user_data = self.get_user_by_id(user_id)

            if product.get_quantity_in_stock() == 0:
                print('Product Unavailable')
                return

            sql = '''
            INSERT INTO Orders(order_id, userId, order_date, total_price, shipping_address)
            VALES(%s, %s, %s, %s, %s)
            '''
            para = (
            get_ids('Orders', 'order_id'), user_data.get_user_id(), date.today(), product.get_price(), shipping_address)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Order Created Successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def cancel_order(self, user_id, order_id):

        try:
            my_cursor = self.connection.cursor()
            sql = '''
                DELETE FROM Orders WHERE order_id = %s AND userId = %s
            '''
            para = (order_id, user_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Order Cancelled successfully')
        except Exception as e:
            print(f'An error occurred: {e}')


