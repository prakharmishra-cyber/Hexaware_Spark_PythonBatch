from db_connector.db_adapter import get_db_connection
from models.teacher import Teacher
from models.enrollment import Enrollment


class Course:

    def __init__(self, course_id, course_name, credit, teacher: Teacher):
        self.connection = get_db_connection()
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credit
        self.__teacher = teacher

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_teacher(self):
        return self.__teacher

    def get_course_credits(self):
        return self.__credits

    def assign_teacher(self, teacher: Teacher):
        my_cursor = self.connection.cursor()
        sql = '''
            UPDATE Courses SET teacher_id = %s WHERE course_id = %s
            '''
        para = (teacher.get_teacher_id(), self.__course_id)
        my_cursor.execute(sql, para)
        self.connection.commit()
        print('Teacher Assigned Successfully')

    def update_course_info(self, course_name=None, credit=None):
        my_cursor = self.connection.cursor()

        if course_name:
            sql = '''
                        UPDATE Courses SET course_name = %s WHERE course_id = %s
                    '''
            para = (course_name, self.__course_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__course_name = course_name

        if credit:
            sql = '''
                        UPDATE Students SET credits = %s WHERE course_id = %s
                    '''
            para = (credit, self.__course_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            self.__credits = credit

        print('Teacher Details Updated Successfully')

    def get_enrollments(self):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * Enrollments WHERE course_id = %s
            '''
            para = (self.__course_id,)
            my_cursor.execute(sql, para)
            x = [Enrollment(*list(i)) for i in list(my_cursor.fetchall())]
        except Exception as e:
            print(f'An error occurred {e}')

    def display_course_info(self):
        print('CourseID', self.__course_id)
        print('Course Name', self.__course_name)
        print('Course Credits', self.__credits)
        print('Teacher Details:-')
        print(self.__teacher)
