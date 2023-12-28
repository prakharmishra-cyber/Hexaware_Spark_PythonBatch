from db_connector.db_adapter import get_db_connection


class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.connection = get_db_connection()
        self.__enrollment_id = enrollment_id
        self.__student = student
        self.__course = course
        self.__enrollment_date = enrollment_date

    def get_enrollment_id(self):
        return self.__enrollment_id

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_enrollment_date(self):
        return self.__enrollment_date

    def display_enrollment_info(self):
        print('Enrollment ID: ', self.__enrollment_id)
        print('Student Details: ', self.__student)
        print('Course Details: ', self.__course)
        print('Enrollment Date: ',self.__enrollment_date)
