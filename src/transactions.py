from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.publickey import PublicKey
from src.raydium_client import create_swap_instruction, send_transaction
from src.config import WALLET1, WALLET2, WALLET3

def swap_tokens(amount, from_token, to_token, signers):
    transaction = Transaction()
    swap_instruction = create_swap_instruction(amount, from_token, to_token)
    transaction.add(swap_instruction)
    response = send_transaction(transaction, signers)
    return response

def transfer_to_wallet(amount, to_wallet, signers):
    transaction = Transaction()
    transfer_instruction = transfer(
        TransferParams(
            from_pubkey=signers[0].public_key(),
            to_pubkey=to_wallet,
            lamports=amount
        )
    )
    transaction.add(transfer_instruction)
    response = send_transaction(transaction, signers)
    return response
