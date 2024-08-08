from src.config import BUY_FEE_PERCENTAGE, SELL_FEE_PERCENTAGE

def calculate_fee(amount, is_buy=True):
    if is_buy:
        fee_percentage = BUY_FEE_PERCENTAGE
    else:
        fee_percentage = SELL_FEE_PERCENTAGE
    return amount * fee_percentage

def get_fees(amount, is_buy=True):
    return calculate_fee(amount, is_buy)
