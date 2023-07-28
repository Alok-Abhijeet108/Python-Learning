import datetime

import pytz


class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance
        self.__transactions = [(balance, Account._current_time())]
        print(f"Acount created for {name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append((amount, Account._current_time()))
            self.show_balance()

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append((-amount, Account._current_time()))
            self.show_balance()
        else:
            print("Not enough money in your account")

    def show_balance(self):
        print(f"Balance is Rs. {self.__balance}")

    def show_transactions(self):
        for amount, date in self.__transactions:
            if amount > 0:
                tran_type = "deposited"
            else:
                amount *= -1
                tran_type = "withdrawn"
            print("{:6} {} at {}".format(amount, tran_type, date.astimezone()))


def fib_memo(n, memo={0: 0, 1: 1}):
    """
    n is the number nth number
    you would like to return in the sequence
    """
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


if __name__ == "__main__":
    alok = Account("Alok Abhijeet", 14995.64)
    alok.withdraw(2500.35)
    Account.deposit(alok, 506.43)
    alok.show_transactions()
    print(alok.__dict__)
