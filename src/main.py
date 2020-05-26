# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    letters_min = 'azxjclptuopwkfr'
    letters_may = letters_min.upper()
    symbols = SYMBOLS

    password_list = []
    len_password = random.randint(2,4)

    for num in range(len_password):
        number = random.randint(0,9)
        password_list.append(str(number))

    for letter in range(len_password):
        password_list.append(random.choice(letters_min))

    for letter in range(len_password):
        password_list.append(random.choice(letters_may))

    for symbol in range(len_password):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list,random.random)
    password = ''.join(password_list)
    print (password)
    print ('# chars = ',len(password))
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
