from datetime import date
from db_connector.db_adapter import get_db_connection
from db_connector.db_adapter import get_ids


class Student:

    def __init__(self, student_id, firstname, lastname, dob, email, phone_number):
        self.connection = get_db_connection()
        self.__student_id = student_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__dob = dob
        self.__email = email
        self.__phone_number = phone_number

    def get_student_id(self):
        return self.__student_id

    def get_first_name(self):
        return self.__firstname

    def get_last_name(self):
        return self.__lastname

    def get_dob(self):
        return self.__dob

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def enroll_in_course(self, course):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                    INSERT INTO Enrollments(enrollment_id, student_id, course_id, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                    '''
            para = (get_ids('enrollments', 'enrollment_id'), self.__student_id, course.get_course_id(), date.today())
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Student Enrolled Successfully')
        except Exception as e:
            print(f'An error occurred {e}')

    def make_payment(self, amount, payment_date):
        try:
            my_cursor = self.connection.cursor()
            sql = '''INSERT INTO Payments(payment_id, student_id, amount, payment_date)
            VALUES (%s, %s, %s, %s)
            '''
            para = (get_ids('payments', 'payment_id'), self.__student_id, amount, payment_date)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Payment Made successfully')
        except Exception as e:
            print(f'An error occurred {e}')

    def get_enrolled_courses(self):
        my_cursor = self.connection.cursor()
        sql = '''
            SELECT * FROM Courses WHERE student_id = %s
        '''
        para = (self.__student_id,)
        my_cursor.execute(sql, para)
        t = list(my_cursor.fetchall())
        x = [list(i) for i in t]
        print(*x, sep='\n')

    def get_payment_history(self):
        my_cursor = self.connection.cursor()
        sql = '''
                    SELECT * FROM Payments WHERE student_id = %s
                '''
        para = (self.__student_id,)
        my_cursor.execute(sql, para)
        t = list(my_cursor.fetchall())
        x = [list(i) for i in t]
        print(*x, sep='\n')

    def display_student_info(self):
        print('StudentID', self.__student_id)
        print('Student First Name', self.__firstname)
        print('Student Last Name', self.__lastname)
        print('Student DOB', self.__dob)
        print('Student Email', self.__email)
        print('Student Phone Number', self.__phone_number)

    def update_student_info(self, first_name=None, last_name=None, date_of_birth=None, email=None, phone_number=None):
        my_cursor = self.connection.cursor()

        if first_name:
            sql = '''
                UPDATE Students SET first_name = %s WHERE student_id = %s
            '''
            para = (first_name, self.__student_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__firstname = first_name

        if last_name:
            sql = '''
                UPDATE Students SET last_name = %s WHERE student_id = %s
            '''
            para = (last_name, self.__student_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__lastname = last_name

        if date_of_birth:
            sql = '''
                UPDATE Students SET date_of_birth = %s WHERE student_id = %s
            '''
            para = (date_of_birth, self.__student_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__dob = date_of_birth

        if email:
            sql = '''
                UPDATE Students SET email = %s WHERE student_id = %s
            '''
            para = (email, self.__student_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__email = email

        if phone_number:
            sql = '''
                UPDATE Students SET phone_number = %s WHERE student_id = %s
            '''
            para = (phone_number, self.__student_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__phone_number = phone_number

        print('Student Details Updated Successfully')
