from db_connector.db_adapter import get_db_connection


class Teacher:

    def __init__(self, teacher_id, firstname, lastname, email):
        self.connection = get_db_connection()
        self.__teacher_id = teacher_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email

    def get_teacher_id(self):
        return self.__teacher_id

    def get_first_name(self):
        return self.__firstname

    def get_last_name(self):
        return self.__lastname

    def get_email(self):
        return self.__email

    def display_teacher_info(self):
        print('TeacherID', self.__teacher_id)
        print('Teacher First Name', self.__firstname)
        print('Teacher Last Name', self.__lastname)
        print('Teacher Email', self.__email)

    def get_assigned_course(self):
        try:
            my_cursor = self.connection.cursor()
            sql = 'SELECT * FROM Course WHERE teacher_id = %s'
            para = (self.__teacher_id,)
            my_cursor.execute(sql, para)
            return list(my_cursor.fetchone())
        except Exception as e:
            print(f'An error occurred: {e}')

    def update_teacher_info(self, first_name=None, last_name=None, email=None):
        my_cursor = self.connection.cursor()

        try:
            sql1 = '''
                UPDATE Teacher SET first_name = %s WHERE teacher_id = %s
            '''
            para1 = (first_name, self.__teacher_id)
            my_cursor.execute(sql1, para1)
            self.connection.commit()
            self.__firstname = first_name
            print('First Name Updated Successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            sql2 = '''
                            UPDATE Teacher SET last_name = %s WHERE teacher_id = %s
                        '''
            para2 = (last_name, self.__teacher_id)
            my_cursor.execute(sql2, para2)
            self.connection.commit()
            self.__lastname = last_name
            print('Last Name Updated Successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            sql3 = '''
                            UPDATE Teacher SET email = %s WHERE teacher_id = %s
                        '''
            para3 = (email, self.__teacher_id)
            my_cursor.execute(sql3, para3)
            self.connection.commit()
            self.__email = email
            print('Email Updated Successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

