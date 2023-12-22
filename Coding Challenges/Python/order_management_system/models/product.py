from db_connector.db_adapter import *


class Product:

    def __init__(self, product_id, product_name, description, price, quantity_in_stock, product_type):
        self.connection = get_db_connection()
        self.__productId = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__quantity_in_stock = quantity_in_stock
        self.__type = product_type

    def get_product_name(self):
        return self.__product_name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_product_type(self):
        return self.__type

    def update_product_info(self, product_name=None, description=None, price=None, quantity_in_stock=None, product_type=None):
        try:
            my_cursor = self.connection.cursor()

            if product_name:
                sql = '''
                UPDATE Product SET productName = %s WHERE productId = %s
                '''
                para = (product_name, self.__productId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Product Name updated successfully')

            if description:
                sql = '''
                UPDATE Product SET description = %s WHERE productId = %s
                '''
                para = (description, self.__productId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Product description updated successfully')

            if price:
                sql = '''
                UPDATE Product SET price = %s WHERE productId = %s
                '''
                para = (price, self.__productId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Product Price updated successfully')

            if quantity_in_stock:
                sql = '''
                UPDATE Product SET quantityInStock = %s WHERE productId = %s
                '''
                para = (quantity_in_stock, self.__productId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Product Quantity_In_Stock updated successfully')

            if product_type:
                sql = '''
                UPDATE Product SET type = %s WHERE productId = %s
                '''
                para = (product_type, self.__productId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Product Type updated successfully')

        except Exception as e:
            print(f'An error occurred: {e}')


