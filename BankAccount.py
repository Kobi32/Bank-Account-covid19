class BankAccount:

    def __init__(self, bal, accountOwner):
        self.balance = bal
        self.accountOwner = accountOwner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Error: Insufficient funds')

    def get_balance(self):
        return self.balance

    def get_accountOwner(self):
        return self.accountOwner

    def __str__(self):
        return 'The balance is ' + format(self.balance, ',.2f')

class BankAccount_INT(BankAccount):

    def __init__(self, balance, accountOwner, accountType):
        BankAccount.__init__(self, balance, accountOwner)
        self.accountType = accountType

    def get_accountType(self):
        return self.accountType

class BankAccount_COVID19(BankAccount):

    def __init__(self, balance, accountOwner, accountType):
        BankAccount.__init__(self, balance, accountOwner)
        self.accountType = accountType

    def get_accountType(self):
        return self.accountType

    def withdraw(self, amount):
        if amount <= 1000:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Error: Insufficient funds')
        else:
            print('You cannot take more than 1000 as per goverment decision !')

class BankAccount_COVID19_company(BankAccount):

    def __init__(self, balance, accountOwner, accountType):
        BankAccount.__init__(self, balance, accountOwner)
        self.accountType = accountType

    def get_accountType(self):
        return self.accountType

    def withdraw(self, amount):
        if amount <= 1000:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Error: Insufficient funds')
        else:
            print('You cannot take more than 1000 as per goverment decision !')