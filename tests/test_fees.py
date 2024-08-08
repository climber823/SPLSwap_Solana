import unittest
from src.fees import calculate_fee

class TestFees(unittest.TestCase):
    
    def test_calculate_fee(self):
        amount = 1000000
        buy_fee = calculate_fee(amount, is_buy=True)
        sell_fee = calculate_fee(amount, is_buy=False)
        self.assertGreater(buy_fee, 0)
        self.assertGreater(sell_fee, 0)

if __name__ == "__main__":
    unittest.main()
