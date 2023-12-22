from services.order_manager import OrderManager
from custom_exception.custome_exceptions import UserNotFound, OrderNotFound
class OrderManagement:

    @staticmethod
    def print_menu():
        print("\nOrder Management System Menu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Cancel Order")
        print("4. Get All Products")
        print("5. Get Order by User")
        print("6. Exit")

    @staticmethod
    def get_user_input():
        return input("\nEnter your choice (1-6): ")

    @staticmethod
    def create_user(order_manager):
        user_id = input("Enter User ID: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role (Admin/User): ")

        order_manager.create_user(user_id, username, password, role)

    @staticmethod
    def create_product(order_manager):
        admin_user_id = input("Enter Admin User ID: ")
        admin_user = order_manager.get_user_by_id(admin_user_id)

        if admin_user and admin_user.get_user_role() == 'Admin':
            product_name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            price = float(input("Enter Product Price: "))
            quantity_in_stock = int(input("Enter Quantity in Stock: "))
            product_type = input("Enter Product Type (Electronics/Clothing): ")

            order_manager.create_product(admin_user, product_name, description, price, quantity_in_stock, product_type)
        else:
            print("Invalid Admin User ID or User is not an admin.")

    @staticmethod
    def cancel_order(order_manager):
        user_id = input("Enter User ID: ")
        order_id = input("Enter Order ID: ")

        try:
            order_manager.cancel_order(user_id, order_id)
        except OrderNotFound as e:
            print(e)
        except UserNotFound as e:
            print(e)

    @staticmethod
    def get_all_products(order_manager):
        products = order_manager.get_all_products()
        print("\nAll Products:")
        for product in products:
            print(f"{product.get_product_name()} - {product.get_price()} - {product.get_quantity_in_stock()} in stock")

    @staticmethod
    def get_order_by_user(order_manager):
        user_id = input("Enter User ID: ")
        orders = order_manager.get_order_by_user(user_id)

        if orders:
            print(f"\nOrders for User ID {user_id}:")
            for order in orders:
                print(f"Order ID: {order.get_order_id()}, Date: {order.get_order_date()}, Total Price: {order.get_total_price()}")
        else:
            print(f"No orders found for User ID {user_id}")

    @staticmethod
    def main():
        order_manager = OrderManager()

        while True:
            OrderManagement.print_menu()
            choice = OrderManagement.get_user_input()

            if choice == "1":
                OrderManagement.create_user(order_manager)
            elif choice == "2":
                OrderManagement.create_product(order_manager)
            elif choice == "3":
                OrderManagement.cancel_order(order_manager)
            elif choice == "4":
                OrderManagement.get_all_products(order_manager)
            elif choice == "5":
                OrderManagement.get_order_by_user(order_manager)
            elif choice == "6":
                print("Exiting Order Management System.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    OrderManagement.main()
