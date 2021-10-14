import unittest
from cans import Cola, OrangeSoda, RootBeer
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
        self.soda_machine = SodaMachine()

    def test_quarter_return_true(self):
        """Test to see if quarter will return True if the register has one"""

        has_coin = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(has_coin)

    def test_dime_return_true(self):
        """Test to see if dime will return True if the register has one"""

        has_coin = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(has_coin)

    def test_nickel_return_true(self):
        """Test to see if nickel will return True if the register has one"""

        has_coin = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(has_coin)

    def test_penny_return_true(self):
        """Test to see if penny will return True if the register has one"""

        returned_coin = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(returned_coin)

    def test_invalid_return_false(self):
        """Test to see if invalid coin will return False"""

        returned_coin = self.soda_machine.register_has_coin('Banana')
        self.assertFalse(returned_coin)


class TestDetermineChangeValue(unittest.TestCase):
    """test to determine change value is correct"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_payment_higher(self):
        """Test to see if change value is correct when payment is higher than cost"""

        total_payment = .5
        soda_price = .4

        returned_change = self.soda_machine.determine_change_value(
            total_payment, soda_price)
        self.assertEqual(returned_change, .1)

    def test_price_higher(self):
        """Test to see if change value is correct when payment is higher than cost"""

        my_orange = OrangeSoda()

        total_payment = .5

        amount_left = self.soda_machine.determine_change_value(
            total_payment, my_orange.price)
        self.assertEqual(amount_left, .1)

    def test_equal_values(self):
        """Test tp determine if two values are equal"""

        my_soda = .5
        my_payment = .5

        no_change = self.soda_machine.determine_change_value(
            my_soda, my_payment)
        self.assertEqual(no_change, 0)


if __name__ == '__main__':
    unittest.main()
