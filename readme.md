# Job Requirements

## Transaction Handling:

### Everything in the Same Transaction: 
All operations (transfers and swaps) must be executed in a single transaction to ensure atomicity.

### Sell All Amount in SOL: 
When selling all of a specified amount in SOL, handle the proceeds in the following manner:
Transfer1: Send a specific amount to wallet1. This transfer takes priority. If the specified amount isn't available, transfer the entire remaining amount.
Transfer2: Send any remaining amount after wallet1 and wallet3 have been funded to wallet2.
Transfer3: Send a percentage fee from the total sell amount to wallet3 if there is enough remaining after covering wallet1.

## Program Functionality:

### Swap SPL Tokens with SOL: 
Write a program that uses the Raydium Router to swap between SPL tokens and SOL. This includes handling both buying and selling operations.

### Fees Handling:
Buy and Sell Fees: Implement fees for both buying and selling, and ensure these fees are handled in SOL.
Fee Deduction: Ensure that fees are taken in SOL and not SPL tokens.

## Integration with Python:

### Raydium Swap Program: 
Use Raydium’s Swap Program and not Jupiter’s. Ensure that fees are not handled by Jupiter’s fee program.

### External Integration: 
The program must expose functions so external sources (like a Python bot) can pull analytics, including fees, total fees, and trade details.

### Python Compatibility: 
The code must be compatible with Python for integration and external interaction.

## Transaction Signing:

### Multiple Signers: 
Ensure that at least two signers are involved in the transactions for security and compliance.

## Program Language:
Only python