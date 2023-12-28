from datetime import date
from db_connector.db_adapter import get_db_connection
from models.course  import Course
from models.payment import Payment
from models.student import Student
from models.enrollment import Enrollment
from models.teacher import Teacher
from db_connector.db_adapter import get_ids
from custom_exception.custom_exceptions import *

class SISManager:

    def __init__(self):
        self.connection = get_db_connection()

    def enroll_student_in_course(self, course: Course, student: Student):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                INSERT INTO Enrollments(enrollment_id, student_id, course_id, enrollment_date)
                VALUES (%s, %s, %s, %s)
            '''
            para = (
            get_ids('enrollments', 'enrollment_id'), student.get_student_id(), course.get_course_id(), date.today())
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Student Enrolled successfully')
        except Exception as e:
            print(f'An error occurred: {e}')

    def assign_teacher_to_course(self, teacher: Teacher, course: Course):
        try:
            course.assign_teacher(teacher)
        except Exception as e:
            print(f'An error occurred: {e}')

    def record_payment(self, student: Student, amount, payment_date):
        try:
            student.make_payment(amount, payment_date)
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_payment_report(self, student: Student):
        try:
            student.get_payment_history()
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_enrollment_report(self, course: Course):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT Students.* FROM Students JOIN Enrollments
                ON Students.student_id = Enrollments.student_id
                WHERE Enrollments.course_id = %s
            '''
            para = (course.get_course_id(),)
            # print(sql, para)
            my_cursor.execute(sql, para)
            x = [list(i) for i in list(my_cursor.fetchall())]
            print(*x)
        except Exception as e:
            print(f'An error occurred: {e}')

    def calculate_course_statistics(self, course: Course):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT SUM(Payments.amount) AS TotalAmount, COUNT(Students.student_id) AS Enrollments FROM Students JOIN Enrollments
                ON Students.student_id = Enrollments.student_id
                JOIN Payments ON Payments.student_id = Students.student_id
                WHERE Enrollments.course_id = %s
            '''
            para = (course.get_course_id(),)
            my_cursor.execute(sql, para)
            x = [list(i) for i in list(my_cursor.fetchall())]
            print(*x, sep='\n')
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_student_by_id(self, student_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Students WHERE student_id = %s
            '''
            para = (student_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise StudentNotFoundException('Invalid Student ID')
            else:
                return Student(*x)
        except StudentNotFoundException as snfe:
            print(f'An error occurred: ', snfe)
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_payment_by_id(self, payment_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Payments WHERE payment_id = %s
            '''
            para = (payment_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise PaymentValidationException('Invalid Payment ID')
            else:
                return Payment(*x)
        except PaymentValidationException as pve:
            print(f'An error occurred: ', pve)
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_course_by_id(self, course_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Courses WHERE course_id = %s
            '''
            para = (course_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise CourseNotFoundException('Invalid Course ID')
            else:
                return Course(*x)
        except CourseNotFoundException as cnfe:
            print(f'An error occurred: ', cnfe)
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_enrollment_by_id(self, enrollment_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Enrollments WHERE enrollment_id = %s
            '''
            para = (enrollment_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise InvalidEnrollmentDataException('Invalid Enrollment ID')
            else:
                return Enrollment(*x)
        except InvalidEnrollmentDataException as infe:
            print(f'An error occurred: ', infe)
        except Exception as e:
            print(f'An error occurred: {e}')

    def get_teacher_by_id(self, teacher_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * FROM Teacher WHERE teacher_id = %s
            '''
            para = (teacher_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise TeacherNotFoundException('Invalid Teacher ID')
            else:
                return Teacher(*x)
        except TeacherNotFoundException as tnfe:
            print(f'An error occurred: ', tnfe)
        except Exception as e:
            print(f'An error occurred: {e}')


