from solana.keypair import Keypair

# Generate a new keypair
keypair = Keypair.generate()

# Print the public key and secret key
print("Public Key:", keypair.public_key)
print("Secret Key:", keypair.secret_key)