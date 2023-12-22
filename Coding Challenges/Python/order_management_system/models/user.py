from db_connector.db_adapter import *


class User:

    def __init__(self, userid, username, password, role):
        self.connection = get_db_connection()
        self.__userId = userid
        self.__user_name = username
        self.__password = password
        self.__role = role

    def get_user_id(self):
        return self.__userId

    def get_user_name(self):
        return self.__user_name

    def get_password(self):
        return self.__password

    def get_user_role(self):
        return self.__role

    def update_user_info(self, username=None, password=None, role=None):
        try:
            my_cursor = self.connection.cursor()

            if username:
                sql = '''
                UPDATE User SET username = %s WHERE userID = %s
                '''
                para = (username, self.__userId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('User Name updated successfully')

            if password:
                sql = '''
                UPDATE User SET password = %s WHERE userID = %s
                '''
                para = (password, self.__userId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('User Password updated successfully')

            if role:
                sql = '''
                UPDATE User SET role = %s WHERE userID = %s
                '''
                para = (role, self.__userId)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('User Role updated successfully')

        except Exception as e:
            print(f'An error occurred: {e}')

    def print_user_info(self):
        print('UserID', self.__userId)
        print('User Name', self.__user_name)
        print('Password', self.__password)
        print('Role', self.__role)


