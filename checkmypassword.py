import hashlib
import requests
import sys


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
    shapassword = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    # splits our password in to two sections
    first5_char, tail = shapassword[:5], shapassword[5:]
    response = request_api_data(first5_char)
    return password_leaks_count(response, tail)


pwned_api_checker('123')


def main(args):
    for password in args:
        count = pwned_api_checker(password)
        if count:
            print(
                f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'finished!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
