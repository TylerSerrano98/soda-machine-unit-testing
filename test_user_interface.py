import unittest
from user_interface import display_payment_value, try_parse_int, validate_coin_selection, validate_main_menu, get_unique_can_names
from cans import Can
from coins import Quarter, Nickel, Dime, Penny


class TestValidateMainMenu(unittest.TestCase):
    """This test determines if input numbers """

    def test_first_option(self):
        """This test is to confirm '1' is returned from tuple"""

        user_types_one = validate_main_menu(1)
        self.assertEqual(user_types_one, (True, 1))

    def test_second_option(self):
        """This test is to confirm '2' is returned from tuple"""

        user_types_two = validate_main_menu(2)
        self.assertEqual(user_types_two, (True, 2))

    def test_third_option(self):
        """This test is to confirm '3' is returned from tuple"""

        user_types_three = validate_main_menu(3)
        self.assertEqual(user_types_three, (True, 3))

    def test_fourth_option(self):
        """This test is to confirm '4' is returned from tuple"""

        user_types_four = validate_main_menu(4)
        self.assertEqual(user_types_four, (True, 4))

    def test_invalid_option(self):
        """This test is to confirm a different number returns (False, None)"""

        user_types_invalid = validate_main_menu(5)
        self.assertEqual(user_types_invalid, (False, None))


class TestTryParseInt(unittest.TestCase):
    """tests to see if string is parse into an integer"""

    def test_int_value_returned(self):
        """test to see if a string number returns an int"""
        random_number = try_parse_int(10)
        self.assertEqual(random_number, 10)

    def test_invalid_string(self):
        """test to see if an invalid string number returns a 0"""
        random_string = try_parse_int("hello")
        self.assertEqual(random_string, 0)


class TestGetUniqueCanNames(unittest.TestCase):
    """test loop through inventory to create list of all distinct types of soda"""

    def test_returned_can_names(self):
        """test to confirm only 3 can names"""
        cola1 = Can("Cola", .7)
        cola2 = Can("Cola", .6)
        orange_soda1 = Can("Orange Soda", .5)
        orange_soda2 = Can("Orange Soda", .4)
        root_beer1 = Can("Root Beer", .3)
        root_beer2 = Can("Root Beer", .2)
        list_of_soda = []

        list_of_soda.append(cola1)
        list_of_soda.append(cola2)
        list_of_soda.append(orange_soda1)
        list_of_soda.append(orange_soda2)
        list_of_soda.append(root_beer1)
        list_of_soda.append(root_beer2)

        total_can_names = get_unique_can_names(list_of_soda)
        self.assertEqual(len(total_can_names), 3)

    def test_pass_empty_list(self):
        """test to confirm passing an empty list returns 0"""
        list_of_soda = []

        total_can_names = get_unique_can_names(list_of_soda)
        self.assertEqual(len(total_can_names), 0)


class TestDisplayPaymentValue(unittest.TestCase):
    """test to see if coins selected by customer is displayed correctly"""

    def test_coin_type_value(self):
        """test to see if coin types return value of .41"""

        my_quarter = Quarter()
        my_nickel = Nickel()
        my_dime = Dime()
        my_penny = Penny()

        list_of_coins = []
        list_of_coins.append(my_quarter)
        list_of_coins.append(my_penny)
        list_of_coins.append(my_dime)
        list_of_coins.append(my_nickel)

        total_value = display_payment_value(list_of_coins)
        self.assertEqual(total_value, .41)

    def test_empty_list_value(self):
        """test to see if empty coin list returns 0"""
        list_of_coins = []

        total_value = display_payment_value(list_of_coins)
        self.assertEqual(total_value, 0)


class TestValidateCoinSelection(unittest.TestCase):
    """Test to validate user coin selection for payment"""

    def test_quarter_validation(self):
        """Test to validate quarter when user inputs '1' """

        user_selects_one = validate_coin_selection(1)
        self.assertEqual(user_selects_one, (True, "Quarter"))

    def test_dime_validation(self):
        """Test to validate dime when user inputs '2' """

        user_selects_two = validate_coin_selection(2)
        self.assertEqual(user_selects_two, (True, "Dime"))

    def test_nickel_validation(self):
        """Test to validate nickel when user inputs '3' """

        user_selects_three = validate_coin_selection(3)
        self.assertEqual(user_selects_three, (True, "Nickel"))

    def test_penny_validation(self):
        """Test to validate penny when user inputs '4' """

        user_selects_four = validate_coin_selection(4)
        self.assertEqual(user_selects_four, (True, "Penny"))

    def test_done_validation(self):
        """Test to validate done when user inputs '5' """

        user_selects_five = validate_coin_selection(5)
        self.assertEqual(user_selects_five, (True, "Done"))

    def test_different_number(self):
        """Test to ensure (False, None) is returned when user inputs different number """

        user_inputs_different = validate_coin_selection(7)
        self.assertEqual(user_inputs_different, (False, None))


if __name__ == '__main__':
    unittest.main()
