import hashlib

import requests


def request_api_data(password_keyword):
    url = 'https://api.pwnedpasswords.com/range/' + password_keyword
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def read_response(response):
    print(response.text)


def pwned_api_checker(password):
    sha256password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha256password[:5], sha256password[5:] # splits our password in to two sections 
    response = request_api_data(first5_char)
    print(response)
    return read_response(response)


pwned_api_checker('123')
