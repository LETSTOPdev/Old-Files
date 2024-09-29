import requests 
import hmac
import hashlib
from urllib.parse import urlencode, quote


# ServerTime、Signature
class TOOL(object):

    def _get_server_time(self):
        return requests.request('get', 'https://api.mexc.com/api/v3/time').json()['serverTime']

    def _sign_v3(self, req_time, sign_params=None):
        if sign_params:
            # Add timestamp to sign_params
            sign_params['timestamp'] = req_time
            to_sign = urlencode(sign_params, quote_via=quote)
        else:
            to_sign = "timestamp={}".format(req_time)

        sign = hmac.new(self.mexc_secret.encode('utf-8'), to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
        return sign

    def public_request(self, method, url, params=None):
        url = '{}{}'.format(self.hosts, url)
        return requests.request(method, url, params=params)

    def sign_request(self, method, url, params=None):
        url = '{}{}'.format(self.hosts, url)
        req_time = self._get_server_time()
        if params:
            params['signature'] = self._sign_v3(req_time=req_time, sign_params=params)
        else:
            params = {}
            params['signature'] = self._sign_v3(req_time=req_time)
        params['timestamp'] = req_time
        headers = {
            'x-mexc-apikey': self.mexc_key,
            'Content-Type': 'application/json',
        }
        return requests.request(method, url, params=params, headers=headers)


class mexc_account(TOOL):

    def __init__(self, mexc_hosts, mexc_key, mexc_secret):
        self.api = '/api/v3'
        self.hosts = mexc_hosts
        self.mexc_key = mexc_key
        self.mexc_secret = mexc_secret

    def get_account_info(self):
        """get account information"""
        method = 'GET'
        url = '{}{}'.format(self.api, '/account')
        response = self.sign_request(method, url)
        return response.json()


class mexc_capital(TOOL):
    def __init__(self, mexc_hosts, mexc_key, mexc_secret):
        self.api = '/api/v3/capital'
        self.hosts = mexc_hosts
        self.mexc_key = mexc_key
        self.mexc_secret = mexc_secret

    def post_transfer_internal(self, params):
        """universal transfer"""
        method = 'POST'
        url = '{}{}'.format(self.api, '/transfer/internal')
        response = self.sign_request(method, url, params=params)
        print(response.url)
        return response.json()

    def get_transfer_internal_list(self, params=None):
        """universal transfer"""
        method = 'GET'
        url = '{}{}'.format(self.api, '/transfer/internal')
        response = self.sign_request(method, url, params=params)
        return response.json()
