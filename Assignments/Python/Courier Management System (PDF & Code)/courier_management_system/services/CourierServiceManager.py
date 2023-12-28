from custom_exceptions.custom_exception import CourierNotFound, TrackingNumberNotFoundException
from db_connection.db_adapter import *
from models.courier import Courier


class CourierService:

    def __init__(self):
        self.connection = get_db_connection()

    @staticmethod
    def add_courier_services(service_id, service_name, cost, employee_id):
        connection = get_db_connection()
        my_cursor = connection.cursor()
        #print(service_id, service_name, cost, employee_id)
        try:
            if not CourierService.is_employee_admin(employee_id):
                raise PermissionError("Only admins can add courier services.")
            sql = '''
                INSERT INTO courierservices (ServiceID, ServiceName, Cost)
                VALUES (%s, %s, %s)
            '''
            para = (service_id, service_name, cost)
            #print(sql, para)
            my_cursor.execute(sql, para)
            connection.commit()
            print('Courier service added successfully.')
        except PermissionError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error adding courier service: {e}')
        finally:
            connection.close()

    @staticmethod
    def is_employee_admin(employee_id):
        admin_counts = get_counts('employee', 'employeeID', 'role', employee_id, 'Admin')
        print(admin_counts)
        return admin_counts > 0

    @classmethod
    def get_courier_by_tracking_no(cls, track_id):
        try:
            mydb = get_db_connection()
            my_cursor = mydb.cursor()
            sql = '''
                SELECT * FROM Courier WHERE TrackingNumber = %s
                '''
            para = (track_id,)
            # print(sql, para)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise TrackingNumberNotFoundException('Invalid Tracking Number')
            else:
                return Courier(*x)
        except TrackingNumberNotFoundException as tnfe:
            print('An error occurred: ', tnfe)
        except Exception as e:
            print('An error occurred: ', e)

    @classmethod
    def cancel_courier(cls, courierID):
        mydb = get_db_connection()
        my_cursor = mydb.cursor()
        courier_exists = get_cnts('courier', 'CourierID', courierID)

        try:
            if courier_exists > 0:
                sql = '''DELETE FROM Courier WHERE CourierID = %s'''
                para = (courier_exists,)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Courier Order deleted successfully')
            else:
                raise CourierNotFound('Invalid Courier ID')
        except CourierNotFound as c:
            print(c)
        except Exception as e:
            print('An error occurred', e)




