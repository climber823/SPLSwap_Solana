import unittest
from src.transactions import swap_tokens, transfer_to_wallet
from solana.publickey import PublicKey

class TestTransactions(unittest.TestCase):
    
    def test_swap_tokens(self):
        amount = 1000000
        from_token = PublicKey("TokenMintAddress1")
        to_token = PublicKey("TokenMintAddress2")
        signers = []  # Add mock signers
        response = swap_tokens(amount, from_token, to_token, signers)
        self.assertIsNotNone(response)
    
    def test_transfer_to_wallet(self):
        amount = 1000000
        to_wallet = PublicKey("YourWallet1Address")
        signers = []  # Add mock signers
        response = transfer_to_wallet(amount, to_wallet, signers)
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
