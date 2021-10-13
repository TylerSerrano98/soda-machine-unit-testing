import unittest
from coins import Dime, Nickel, Penny, Quarter
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """test for soda machines fill_register method"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_length(self):
        """test to see if register length is 88"""
        self.assertEqual(88, len(self.soda_machine.register))

class TestFillInventory(unittest.TestCase):
    """test for soda machines fill_inventory method"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_inventory_length(self):
        """test to see if inventory length is 30"""
        my_inventory = SodaMachine()
        self.assertEqual(30, len(self.soda_machine.inventory))

class TestGetCoinFromRegister(unittest.TestCase):
    """test for soda machines get_coin_from_register method"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_quarter_return(self):
        """test to see if quarter can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertIsInstance(returned_coin, Quarter)

    def test_register_nickel_return(self):
        """test to see if nickel can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertIsInstance(returned_coin, Nickel)

    def test_register_dime_return(self):
        """test to see if dime can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertIsInstance(returned_coin, Dime)

    def test_register_penny_return(self):
        """test to see if penny can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertIsInstance(returned_coin, Penny)

    def test_register_return_none(self):
        """test to see if invalid coin name returns none"""
        returned_coin = self.soda_machine.get_coin_from_register('banana')
        self.assertEqual(returned_coin, None)

    
class TestRegisterHasCoin(unittest.TestCase):
    """test to see if register has each type of coin"""
    def setUp(self):
        pass
        
    

if __name__ == '__main__':
    unittest.main()