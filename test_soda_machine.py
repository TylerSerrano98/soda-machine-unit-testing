import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """test for soda machines fill_register method"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_length(self):
        """test to see if register length is 88"""
        my_register = SodaMachine()
        self.assertEqual(88, len(self.soda_machine.register))

class TestFillInventory(unittest.TestCase):
    """test for soda machines fill_inventory method"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_inventory_length(self):
        """test to see if inventory length is 30"""
        my_inventory = SodaMachine()
        self.assertEqual(30, len(self.soda_machine.inventory))
    

if __name__ == '__main__':
    unittest.main()