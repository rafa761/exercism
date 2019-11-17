import threading
import concurrent.futures


class BankAccount:
    def __init__(self):
        pass

    def get_balance(self):
        return self.__balance

    def open(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def close(self):
        pass


if __name__ == "__main__":
    conta = BankAccount()
    conta.open()
    conta.deposit(1000)
    print(conta.get_balance())
