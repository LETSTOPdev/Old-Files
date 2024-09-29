
import json
import os
import mexc_api_funcs

mexc_key = os.environ['MEXC_API_KEY']
mexc_secret = os.environ['MEXC_SECRET_KEY']
hosts = "https://api.mexc.com"
transfer_account = mexc_api_funcs.mexc_capital(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret)
account = mexc_api_funcs.mexc_account(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret)



def lambda_handler(event, context):
    user_id = event.get('user_id')
    amount = event.get('amount')
    if user_id is None or amount is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User ID and amount are required in the event'})
        }
    result_transfer = transfer(user_id, "USDT", amount)
    # check if transfer was successful by checking if tranId is in the response
    if 'tranId' in result_transfer:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"Transfer of {amount}  to user {user_id} was successful with tranId {result_transfer['tranId']}"})
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"Transfer of {amount} to user {user_id} failed"})
        }


def get_symbol_balance(symbol) -> float:
    """Get the balance of a symbol in your account
    :param symbol: str (e.g. "USDT")
    :return: float (e.g. 100.0)
    """
    res = account.get_account_info()
    res = res['balances']
    symbol_b = next((item for item in res if item['asset'] == symbol), None)
    if symbol_b is not None:
        return float(symbol_b['free'])
    else:
        print(f"{symbol} not found in balances")
        return 0.0


def transfer(user_id, symbol, amount):
    """Transfer a specified amount of a symbol to a user's account
    :param user_id: str (e.g. "49680184")
    :param symbol: str (e.g. "USDT")
    :param amount: float (e.g. 100.0)
    :returns: dict (e.g. {'tranId':12gdsf13r124})
    """
    # convert amount to float
    amount = float(amount)
    if amount <= 0:
        return "Amount should be positive"
    elif get_symbol_balance(symbol) < amount:
        return f"Insufficient balance for {symbol}"
    else:
        res = transfer_account.post_transfer_internal(
            params={"toAccountType": "UID", "toAccount": user_id, "asset": symbol, "amount": str(amount)})
    return res

