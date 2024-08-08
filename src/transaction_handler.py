from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer
from src.config import SOLANA_RPC_ENDPOINT
from src.raydium_swap import swap_tokens
from src.fees_handler import calculate_fees

client = Client(SOLANA_RPC_ENDPOINT)

def handle_transaction(data):
    amount = data['amount']
    sell_token = data['sell_token']
    wallet1 = PublicKey(data['wallet1'])
    wallet2 = PublicKey(data['wallet2'])
    wallet3 = PublicKey(data['wallet3'])
    fee_percentage = data['fee_percentage']
    
    # Swap SPL tokens for SOL
    swap_amount = amount
    swap_tokens(sell_token, swap_amount)
    
    # Calculate fees
    total_fees = calculate_fees(amount, fee_percentage)
    
    # Create transaction
    transaction = Transaction()
    transaction.add(
        transfer(
            TransferParams(
                from_pubkey=wallet1,
                to_pubkey=wallet1,
                lamports=amount
            )
        )
    )
    transaction.add(
        transfer(
            TransferParams(
                from_pubkey=wallet1,
                to_pubkey=wallet2,
                lamports=amount - total_fees
            )
        )
    )
    transaction.add(
        transfer(
            TransferParams(
                from_pubkey=wallet1,
                to_pubkey=wallet3,
                lamports=total_fees
            )
        )
    )
    
    # Sign and send transaction
    payer = Keypair()
    transaction.sign(payer)
    response = client.send_transaction(transaction, payer, opts={'skip_confirmation': False})
    return response
