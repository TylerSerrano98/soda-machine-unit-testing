import unittest
from user_interface import validate_main_menu


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


if __name__ == '__main__':
    unittest.main()
