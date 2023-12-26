import unittest
from custom_exceptions.custom_exceptions import CustomerNotFoundException, VehicleNotFoundException, \
    LeaseNotFoundException
from services.lease_manager import LeaseManager
from services.vehicle_manager import VehicleManager
from services.payment_manager import PaymentManager
from services.customer_manager import CustomerManager


class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.lease_manager = LeaseManager()
        self.vehicle_manager = VehicleManager()
        self.payment_manager = PaymentManager()
        self.customer_manager = CustomerManager()

    @unittest.skip
    def test_create_vehicle_success(self):
        x = self.vehicle_manager.add_vehicle('Toyota', 'Camry', 2022, 50.0, 'available', 5, 2500)
        self.assertIsInstance(x, int)
        self.assertGreater(x, 0)

    @unittest.skip
    def test_create_lease_success(self):
        x = self.lease_manager.create_lease(11, 1, '2023-12-26', '2023-12-31', 'Daily')

        self.assertIsInstance(x, int)
        self.assertGreater(x, 0)


    def test_exception_customer_not_found(self):
        with self.assertRaises(CustomerNotFoundException):
            self.customer_manager.get_customer_by_id(999)

    def test_exception_vehicle_not_found(self):
        with self.assertRaises(VehicleNotFoundException):
            self.vehicle_manager.find_vehicle_by_id(999)

    def test_exception_lease_not_found(self):
        with self.assertRaises(LeaseNotFoundException):
            self.lease_manager.get_lease_by_id(999)


if __name__ == '__main__':
    unittest.main()
