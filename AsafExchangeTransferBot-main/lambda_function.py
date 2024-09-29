import os
import time
import mexc_api_funcs
import json

mexc_key = os.environ['MEXC_API_KEY']
mexc_secret = os.environ['MEXC_SECRET_KEY']
hosts = "https://api.mexc.com"
transfer_account = mexc_api_funcs.mexc_capital(mexc_hosts=hosts, mexc_key=mexc_key, mexc_secret=mexc_secret)

def lambda_handler(event, context):
    tranid = event.get('tranid')
    ten_minutes_in_ms = 10 * 60 * 1000
    # Get the current timestamp in milliseconds
    current_timestamp = int(time.time() * 1000)
    response = transfer_account.get_transfer_internal_list(params={"tranId": tranid})
    # Filter the data
    filtered_data = [
        transaction
        for transaction in response["data"]
        if (current_timestamp - transaction["timestamp"] <= ten_minutes_in_ms)
           and transaction["tranId"] == tranid
    ]
    # Check if any transactions were found
    if filtered_data:
        return json.dumps(filtered_data[0]['tranId'])

    else:
        return json.dumps(0)
