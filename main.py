from src.transaction_handler import handle_transaction
from src.external_interface import get_trade_details

def main():
    # Example usage
    transaction_data = {
        'amount': 100,  # Example amount in SOL
        'sell_token': 'wCgBnpuQkrAjcx7N7nt1pN2HToSKxGyqhCybAC37KPa',
        'wallet1': 'BoKBjzRLazea8HomSsbCkFBnhvk5BCuxSR3KHSbiAQwh',
        'wallet2': '7z5pXE6JYHRC4f2Xk4XkLBHP9ZK51Hz33jt8ssEBWhzY',
        'wallet3': 'GaYjzPZDptU9PkNfEdWUruNyTErBRuytMo6pM2VJawv9',
        'fee_percentage': 0.01  # 1% fee
    }
    
    # Handle transaction
    result = handle_transaction(transaction_data)
    print(result)
    
    # Print trade details
    trade_details = get_trade_details()
    print(trade_details)

if __name__ == '__main__':
    main()
