import unittest
from customer import Customer
from coins import Quarter, Nickel, Dime


class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, 0.25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, 0.10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, 0.05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, 0.01)

    def test_can_return_none(self):
        """Pass in not a valid string, method should return a none"""
        returned_coin = self.customer.get_wallet_coin('banana')
        self.assertEqual(returned_coin, None)


class TestAddCoinsToWallet(unittest.TestCase):
    """Test for add_coins_to_wallet method"""

    def setUp(self):
        self.customer = Customer()

    def test_list_of_coins(self):
        """Test that the len of customers wallets money list went up by 3"""
        my_quarter = Quarter()
        my_dime = Dime()
        my_nickel = Nickel()
        list_of_coins = [my_quarter, my_dime, my_nickel]
        self.customer.add_coins_to_wallet(list_of_coins)
        self.assertEqual(91, len(self.customer.wallet.money))

    def test_empty_list_of_coins(self):
        """Test that the len of customers wallets money list to see that it remained the same"""
        my_quarter = Quarter()
        my_dime = Dime()
        my_nickel = Nickel()
        list_of_coins = []
        self.customer.add_coins_to_wallet(list_of_coins)
        self.assertEqual(88, len(self.customer.wallet.money))


if __name__ == '__main__':
    unittest.main()
