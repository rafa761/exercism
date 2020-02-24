import re


def verify(isbn=str):
    # Remove hifen and set lower
    isbn = isbn.lower().replace('-', '')

    # Check if there is a letter in isbn, also check if there ends with a char not than X
    if re.match(r'([0-9]+[a-z][0-9]|.*[^x|^[0-9]$)', isbn):
        return False

    # Check length to identify invalid cod
    cod_len = len(isbn)
    if cod_len != 10:
        return False

    else:
        # check if end with x
        end_x = bool(isbn.endswith('x'))

        # Remove x
        isbn = isbn.replace('x', '0')

        # Add 10 if the isbn ends with x
        sum_x = 10 if end_x else 0

        validation_list = []

        count = 10

        for num in isbn:
            validation_list.append(int(num) * count)
            count -= 1

        return (sum(validation_list) + sum_x) % 11 == 0
