import requests


def request_api_data(password_keyword):
    url = 'https://api.pwnedpasswords.com/range/' + password_keyword
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


request_api_data('CDBFE')  # the api only takes hashed password, testing if it raises any error
