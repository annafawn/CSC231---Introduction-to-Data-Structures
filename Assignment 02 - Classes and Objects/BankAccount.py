class BankAccount:
    def __init__(self, acct_num, first_name, last_name, balance):
        self.acct_num = acct_num
        self.first_name = first_name
        self.last_name = last_name
        self.balance = float(balance)

    def __str__(self):
        return self.acct_num + ", " + self.last_name + ", " + self.first_name + ": " + str(self.balance)

    def __eq__(self, other):
        if type(other) == type(self):
            if self.acct_num == other.acct_num:
                return True
        return False

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

class CheckingAccount(BankAccount):
    def calculate_interest(self):
        return 0.015 * self.balance

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 0.025 * self.balance