import random
import string


class Robot(object):
    word_list = string.ascii_uppercase
    number_list = string.digits

    def __init__(self):
        self.name = self.get_name()

    def get_name(self):
        temp_name = random.choices(self.word_list, k=2) + random.choices(self.number_list, k=3)
        self.name = ''.join(temp_name)

    def reset(self):
        self.old_name = self.name
        while self.name == self.old_name:
            self.name = self.get_name()
