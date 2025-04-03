import unittest
from CleansingTransformation import CustomerTransactionsCleaner

class TestCustomerTransactionsCleaner(unittest.TestCase):

    def test_is_valid_email(self):
        # Test valid emails
        self.assertTrue(CustomerTransactionsCleaner.is_valid_email("test@example.com", None))
        self.assertTrue(CustomerTransactionsCleaner.is_valid_email("john.doe@example.co.uk", None))

        # Test invalid emails
        self.assertFalse(CustomerTransactionsCleaner.is_valid_email("invalid-email", None))
        self.assertFalse(CustomerTransactionsCleaner.is_valid_email("another@invalid", None))

    def test_is_valid_date(self):
        # Test valid date
        self.assertTrue(CustomerTransactionsCleaner.is_valid_date("2023-01-01", "%Y-%m-%d"))

        # Test invalid date
        self.assertFalse(CustomerTransactionsCleaner.is_valid_date("invalid_date", "%Y-%m-%d"))
        self.assertFalse(CustomerTransactionsCleaner.is_valid_date("2023-13-01", "%Y-%m-%d"))

    def test_standardize_category(self):
        # Test category standardization
        self.assertEqual(CustomerTransactionsCleaner.standardize_category("Electronics "), "electronics")
        self.assertEqual(CustomerTransactionsCleaner.standardize_category(" Home_Appliances"), "home_appliances")
        self.assertEqual(CustomerTransactionsCleaner.standardize_category("  Fashion "), "fashion")

if __name__ == "__main__":
    unittest.main()
