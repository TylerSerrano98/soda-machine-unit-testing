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
        """Test to determine if two values are equal"""

        my_soda = .5
        my_payment = .5

        no_change = self.soda_machine.determine_change_value(
            my_soda, my_payment)
        self.assertEqual(no_change, 0)


class TestCalculateCoinValue(unittest.TestCase):
    """test to determine calculated coin value"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_coin_value_return(self):
        """Test to see if coin types appended to list equal a value of .41"""
        my_quarter = Quarter()
        my_nickel = Nickel()
        my_dime = Dime()
        my_penny = Penny()

        list_of_coins = []
        list_of_coins.append(my_quarter)
        list_of_coins.append(my_penny)
        list_of_coins.append(my_dime)
        list_of_coins.append(my_nickel)
        total_value = self.soda_machine.calculate_coin_value(list_of_coins)
        self.assertEqual(total_value, .41)

    def test_coin_value_zero(self):
        """Test to see if empty list returns a value of 0"""
        list_of_coins = []
        total_value = self.soda_machine.calculate_coin_value(list_of_coins)
        self.assertEqual(total_value, 0)


class TestGetInventorySoda(unittest.TestCase):
    """test to determine the inventory of soda"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_cola_name(self):
        """test to determine if cola returns cola"""
        my_cola = self.soda_machine.get_inventory_soda("Cola")
        self.assertIsInstance(my_cola, Cola)

    def test_orange_name(self):
        """test to determine if Orange soda returns Orange soda"""
        my_orange = self.soda_machine.get_inventory_soda("Orange Soda")
        self.assertIsInstance(my_orange, OrangeSoda)

    def test_root_beer_name(self):
        """test to determine if Root beer returns Root beer"""
        my_root_beer = self.soda_machine.get_inventory_soda("Root Beer")
        self.assertIsInstance(my_root_beer, RootBeer)

    def test_invalid_name(self):
        """test to determine if Invalid soda returns None"""
        my_soda = self.soda_machine.get_inventory_soda("Mountain Dew")
        self.assertEqual(my_soda, None)


class TestReturnInventory(unittest.TestCase):
    """test to determine if can is returned to inventory"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_return_can_list_length(self):
        """Test to see if length of self.inventory is 31 after returned can"""

        returned_can = Cola()
        self.soda_machine.return_inventory(returned_can)
        self.assertEqual(len(self.soda_machine.inventory), 31)


class TestDepositCoinsIntoRegister(unittest.TestCase):
    """test to determine if coins are being passed into the register"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_length_of_register(self):
        """This test determines if passed in coins will be added to the register list"""
        my_quarter = Quarter()
        my_nickel = Nickel()
        my_dime = Dime()
        my_penny = Penny()

        list_of_coins = []
        list_of_coins.append(my_quarter)
        list_of_coins.append(my_penny)
        list_of_coins.append(my_dime)
        list_of_coins.append(my_nickel)

        self.soda_machine.deposit_coins_into_register(
            list_of_coins)
        self.assertEqual(len(self.soda_machine.register), 92)


if __name__ == '__main__':
    unittest.main()
