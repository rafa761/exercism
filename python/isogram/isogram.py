# Module with useful string methods
from string import ascii_lowercase


def is_isogram(string):
    char_dict = {}
    # Count the chars in string and update in the char dict
    for char in str(string).lower():
        if char in ascii_lowercase:
            char_dict.update({char: str(string).lower().count(char)})

    return all(value == 1 for key, value in char_dict.items())
    # This doesn't worked
    # if all(list(map(lambda x: x == 1, char_dict))):
    #     return True
    # else:
    #     return False
