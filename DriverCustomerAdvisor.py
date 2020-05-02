import BankAccount
import csv
import os

def main():

    menuSelection = None

    while menuSelection != 3:

        ShowMainMenu()
        menuSelection = int(input("Option number: "))

        if menuSelection == 1:

            ShowAccountOptions()
            accountSelection = int(input("Option number: "))

            print('Enter the following data for new account.')
            balance = float(input('Start Balance: '))
            accountOwner = input('Account Owner: ')

            if accountSelection == 1:
                accountType = 'regular'
                account = BankAccount.BankAccount_COVID19(balance, accountOwner,accountType)
            elif accountSelection == 2:
                accountType = 'forgin'
                account = BankAccount.BankAccount_INT(balance, accountOwner,accountType)
            elif accountSelection == 3:
                accountType = 'company'
                account = BankAccount.BankAccount_COVID19_company(balance + 5000, accountOwner,accountType)

            BankOperations(account)

        if menuSelection == 2:
            print('Enter account owner name. (Please note that file should be in the same folder as project)')
            accountOwnerName = input('Account Owner: ')
            account = LoadAccountData(accountOwnerName)
            BankOperations(account)

def ShowMainMenu():

    print("")
    print("Please select option:")
    print("1.Create account")
    print("2.Load account from file")
    print("3.Quit")
    print("")

def ShowAccountOptions():

    print("")
    print("Please select account type:")
    print("1.Regular account")
    print("2.Forgin customer account")
    print("3.Company account")
    print("")

def ShowOperationOptions():

    print("")
    print('Operation options:')
    print("1.Save data to file")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Close account")
    print("5.Show current balance")
    print("6.Go to main menu")
    print("")

def SaveAccountData(account):
    with open(account.get_accountOwner() + '.csv', mode='w') as bank_file:
        account_writer = csv.writer(bank_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        account_writer.writerow([account.get_balance(), account.get_accountOwner(), account.get_accountType()])

def DepositMoney(account):
    print('How much you would like to deposit:')
    cash = float(input('Deposit Value: '))
    account.deposit(cash)

def WithdrawMoney(account):
    print('How much you would like to withdraw:')
    cash = float(input('Withdraw Value: '))
    account.withdraw(cash)

def CloseAccount(account):
    accountType = account.get_accountType()
    if accountType == 'company':
        print('You cannot close this type of account !')
    else:
        closeAccount = account.get_balance()
        account.withdraw(closeAccount)
        if os.path.exists(account.get_accountOwner() + '.csv'):
            os.remove(account.get_accountOwner() + '.csv')
        print('This account is deleted')

def LoadAccountData(accountOwnerName):
    with open(accountOwnerName + '.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                print('')
                print(f'Account Balance: {row[0]} Account Owner: {row[1]} Account Type: {row[2]}')

                if row[2] == "regular":
                    account = BankAccount.BankAccount_COVID19(float(row[0]), row[1],row[2])
                    return account
                elif row[2] == "forgin":
                    account = BankAccount.BankAccount_INT(float(row[0]), row[1], row[2])
                    return account
                elif row[2] == "company":
                    account = BankAccount.BankAccount_COVID19_company(float(row[0]), row[1], row[2])
                    return account

def BankOperations(account):

    accountOperations = None
    while accountOperations != 6:
        ShowOperationOptions()
        accountOperations = int(input("Option number: "))
        if accountOperations == 1:
            SaveAccountData(account)
        elif accountOperations == 2:
            DepositMoney(account)
        elif accountOperations == 3:
            WithdrawMoney(account)
        elif accountOperations == 4:
            CloseAccount(account)
            del account
            break
        elif accountOperations == 5:
            print(account)

main()