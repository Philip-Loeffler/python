import datetime
import pytz


class Account:
    # simple account class with balance

    # this is a static method - static method is shared by all instances of the class
    # you add this anotation in front of it to indicate that it is a static method
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append(
                (Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), - amount))
        else:
            print(
                "the amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(
                amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
    tim.withdraw(2000)

    tim.show_transaction()
