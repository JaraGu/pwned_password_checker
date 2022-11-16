import hashlib

import requests


def request_api_data(password_keyword):
    url = 'https://api.pwnedpasswords.com/range/' + password_keyword
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def password_leaks_count(hashes, hatb_checked):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hatb_checked:
      return count
  return 0


def pwned_api_checker(password):
    sha256password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha256password[:5], sha256password[5:] # splits our password in to two sections 
    response = request_api_data(first5_char)
    return password_leaks_count(response, tail)



pwned_api_checker('123')
