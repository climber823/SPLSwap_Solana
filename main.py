from solana.keypair import Keypair
from src.transactions import swap_tokens, transfer_to_wallet
from src.fees import get_fees
from src.config import WALLET1, WALLET2, WALLET3
from solana.publickey import PublicKey

def main():
    # Example swap amount and token addresses
    swap_amount = 1000000  # Amount in lamports
    from_token = PublicKey("TokenMintAddress1")
    to_token = PublicKey("TokenMintAddress2")

    # Load signers (you should securely handle private keys)
    signers = [Keypair() for _ in range(2)]

    # Perform the swap
    swap_response = swap_tokens(swap_amount, from_token, to_token, signers)
    
    # Calculate fees
    buy_fee = get_fees(swap_amount, is_buy=True)
    sell_fee = get_fees(swap_amount, is_buy=False)

    # Check if the swap amount is sufficient after fees
    if swap_amount > buy_fee + sell_fee:
        transfer_to_wallet(swap_amount - buy_fee - sell_fee, WALLET1, signers)
        transfer_to_wallet(buy_fee, WALLET3, signers)
        transfer_to_wallet(sell_fee, WALLET2, signers)
    else:
        print("Insufficient amount to cover fees")

    print(f"Swap Response: {swap_response}")

if __name__ == "__main__":
    main()
