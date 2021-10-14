import unittest
from user_interface import try_parse_int, validate_main_menu, get_unique_can_names
from cans import Can


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
    

        


if __name__ == '__main__':
    unittest.main()
