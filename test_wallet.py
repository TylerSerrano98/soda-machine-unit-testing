import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """test for wallet fill_wallet method"""
    
    def setUp(self):
        self.wallet = Wallet()

    def test_money_length(self):
        """test that wallets money len is a value of 88"""
        my_wallet = Wallet()
        self.assertEqual(88, len(self.wallet.money))
    
if __name__ == '__main__':
    unittest.main()