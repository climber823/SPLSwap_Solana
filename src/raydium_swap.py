from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction
from solana.keypair import Keypair
from solana.rpc.commitment import Confirmed
from solana.transaction import AccountMeta
from src.config import RAYDIUM_SWAP_PROGRAM_ID, SOLANA_RPC_ENDPOINT

client = Client(SOLANA_RPC_ENDPOINT)

def swap_tokens(sell_token: str, amount: int):
    # Sign the transaction with the user's keypair
    user_keypair = Keypair.from_secret_key(b'R|\x8a\xda\xd8\xd9\x01!\x7f:9kK\xdf\xf0\xae\x9f\xda\x80\xd4\xb1\x83\xb6\xaa\xd3\xaf\x0bl:\x95\xa1u\x10\xd8`\xcb\x86\xb4\xda)x\x87X-*H\xe3\xa6V\xa0\xeb\x1d\x16\x89oI\xb2\xe0\xa2R\xdfg\xa8,')  # Replace with your actual secret key
    
    # Placeholder public keys, replace with actual keys
    source_token_account = PublicKey("2RTfZreov8Vg4otZqBcpgz8QEcd6TovE6P3vqCJ9znat")
    destination_token_account = PublicKey("D8QvSdyyRg43abSqfAtAe3pgXJhxyNFXTwHnu4QvdZp1")
    user_transfer_authority = Keypair().public_key

    # Raydium Swap Program's public key
    raydium_program_id = PublicKey(RAYDIUM_SWAP_PROGRAM_ID)

    # Create the swap instruction
    swap_instruction = TransactionInstruction(
        keys=[
            AccountMeta(pubkey=source_token_account, is_signer=False, is_writable=True),
            AccountMeta(pubkey=destination_token_account, is_signer=False, is_writable=True),
            AccountMeta(pubkey=user_transfer_authority, is_signer=True, is_writable=False),
        ],
        program_id=raydium_program_id,
        data=amount.to_bytes(5, 'little')  # Encode the amount as a byte array
    )

    # Create the transaction and add the swap instruction
    transaction = Transaction()

    # Fetch a recent blockhash
    recent_blockhash = client.get_recent_blockhash()["result"]["value"]["blockhash"]

    # Add the recent blockhash and fee payer to the transaction
    transaction.recent_blockhash = recent_blockhash
    transaction.fee_payer = user_keypair.public_key
    transaction.add(swap_instruction)

    print(user_keypair.public_key)

    # Sign the transaction
    transaction.sign(user_keypair)

    # Send the transaction
    response = client.send_transaction(transaction, user_keypair)

    # Wait for confirmation
    client.confirm_transaction(response['result'], commitment=Confirmed)

    return response
