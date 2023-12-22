from db_connector.db_adapter import get_db_connection


class Order:

    def __init__(self, order_id, user_id, order_date, total_price, shipping_address):
        self.connection = get_db_connection()
        self.__order_id = order_id
        self.__user_id = user_id
        self.__order_date = order_date
        self.__total_price = total_price
        self.__shipping_address = shipping_address

    def get_order_id(self):
        return self.__order_id

    def get_customer_id(self):
        return self.__user_id

    def get_order_date(self):
        return self.__order_date

    def get_total_price(self):
        return self.__total_price

    def get_shipping_address(self):
        return self.__shipping_address

    def update_order_info(self, user_id=None, order_date=None, total_price=None, shipping_address=None):
        try:
            my_cursor = self.connection.cursor()

            if user_id:
                sql = '''
                UPDATE Orders SET userId = %s WHERE order_id = %s
                '''
                para = (user_id, self.__order_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('User ID updated successfully')

            if order_date:
                sql = '''
                UPDATE Orders SET order_date = %s WHERE order_id = %s
                '''
                para = (order_date, self.__order_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Order date updated successfully')

            if total_price:
                sql = '''
                UPDATE Orders SET total_price = %s WHERE order_id = %s
                '''
                para = (total_price, self.__order_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Total price updated successfully')

            if shipping_address:
                sql = '''
                UPDATE Orders SET shipping_address = %s WHERE order_id = %s
                '''
                para = (shipping_address, self.__order_id)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Shipping address updated successfully')

        except Exception as e:
            print(f'An error occurred: {e}')

    def print_order_info(self):
        print(f'Order ID: {self.__order_id}')
        print(f'User ID: {self.__user_id}')
        print(f'Order Date: {self.__order_date}')
        print(f'Total Price: {self.__total_price}')
        print(f'Shipping Address: {self.__shipping_address}')
