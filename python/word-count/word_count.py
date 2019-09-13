# Module to work with Regular expression
import re


def word_count(phrase):
    # Initialize the dict to store words
    word_dict = {}

    # Match the phrase words
    word_list = re.findall(r"(\w+?'\w+|\w+)", phrase.lower().replace('_', ' '))

    # Iterate through words counting
    for word in word_list:
        word_dict.update({word: word_list.count(word)})
    return word_dict
