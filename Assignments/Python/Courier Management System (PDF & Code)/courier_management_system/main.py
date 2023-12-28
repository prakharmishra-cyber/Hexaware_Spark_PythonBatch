from models.courier import Courier
from services.CourierServiceManager import CourierService
from datetime import datetime

class CourierSystemMenu:
    def __init__(self):
        self.courier_service = CourierService()

    def display_menu(self):
        while True:
            print("\nCourier System Menu:")
            print("1. Place Courier Order")
            print("2. Check Order Status")
            print("3. Cancel Courier Order")
            print("4. Add Courier Service (Admin)")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.place_courier_order()
            elif choice == "2":
                self.check_order_status()
            elif choice == "3":
                self.cancel_courier_order()
            elif choice == "4":
                self.add_courier_service()
            elif choice == "5":
                print("Exiting Courier System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def place_courier_order(self):

        sender_name = input("Enter sender name: ")
        sender_address = input("Enter sender address: ")
        receiver_name = input("Enter receiver name: ")
        receiver_address = input("Enter receiver address: ")
        weight = float(input("Enter weight: "))
        status = "Yet to Transit"
        tracking_number = Courier.generate_tracking_number()
        delivery_date = input("Enter delivery date (YYYY-MM-DD): ")

        Courier.place_courier(sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, datetime.strptime(delivery_date, "%Y-%m-%d").date())
        print(f"Courier order placed successfully. Tracking Number: {tracking_number}")

    def check_order_status(self):
        tracking_number = input("Enter tracking number: ")
        temp_courier = CourierService.get_courier_by_tracking_no(track_id=tracking_number)
        print(f"Order Status: {temp_courier.get_status()}")

    def cancel_courier_order(self):
        courier_id = input("Enter Courier ID: ")
        CourierService.cancel_courier(courier_id)

    def add_courier_service(self):
        employee_id = input("Enter admin employee ID: ")
        if self.courier_service.is_employee_admin(employee_id):
            employee_id2 = (input("Enter Employee ID: "))
            service_id = (input("Enter service ID: "))
            service_name = input("Enter service name: ")
            cost = (input("Enter cost: "))
            self.courier_service.add_courier_services(service_id, service_name, cost, employee_id2)
        else:
            print("Error: Only admins can add courier services.")

if __name__ == "__main__":
    menu = CourierSystemMenu()
    menu.display_menu()
