from bank import Bank, SavingsAccount


# Implementation of ATM class
class ATM(object):
    '''This class represents terminal-based
    ATM transactions.'''

    # Implementation of __init__
    def __init__(self, bank):
        self._account = None

    self._bank = bank
    self._methods = {}  # Jump table for commands
    self._methods["1"] = self._getBalance
    self._methods["2"] = self._deposit
    self._methods["3"] = self._withdraw
    self._methods["4"] = self._quit

    # Implementation of run method
    def run(self):
        '''Logs in users and processes their accounts.'''

    failureCount = 0
    # Iterate the loop
    while True:
    # Prompt user to enter name
    userName = raw_input("Enter Name : ")
    # Prompt user to enter PIN
    pin = raw_input("Enter PIN : ")
    # Load account
    self._account = self._bank.get(pin)
    # If account was not found
    # Print "Error, unrecognized PIN"
    if (self._account == None):
    # Display statement
    print("Error, unrecognized PIN")
    failureCount += 1
    # If account name does not match name
    # Print "Error, unrecognized name"
    elif (self._account.getName() != userName):


# Display statement
print("Error, unrecognized name")
# Increment the failureCount
failureCount += 1
# If account is valid
# Load account menu
else:
self._processAccount()
# If an invalid entry was made three times
# Print "Shutting down and calling the cops!" and end program
if (failureCount >= 3):
# Display statement
print("Shutting down and calling the cops!")
return


# Implementation of _processAccount method
def _processAccount(self):



# Iterate the loop
while True:
# Display statement
print("1 View your balance")
print("2 Make a deposit")
print("3 Make a withdrawal")
print("4 Quit\n")
# Get the number from user
number = raw_input("Enter a number: ")
theMethod = self._methods.get(number, None)
# check theMethod is equal to None or not
if theMethod == None:
# Display statement
print("Unrecognized number")
else:
theMethod()
if self._account == None:
    break


# Implementation of _getBalance method
def _getBalance(self):


# Display statement
print("Your balance is $", self._account.getBalance())


# Implementation of _deposit method
def _deposit(self):


# Get the amount from user

amount = "oat(raw_input("Enter the amount to deposit: "))
self._account.deposit(amount)


# Implementation of _withdraw method
def _withdraw(self):


# Get the amount from user
amount = "oat(raw_input(" Enter the amount to withdraw: "))
message = self._account.withdraw(amount)
if message:
# Display statement
print(message)


# Implementation of _quit method
def _quit(self):
    self._bank.save()


self._account = None
# Display statement
print("Have a nice day!")


# Top-level functions
# Implementation of main metthod
def main():
    '''Instantiate an ATM and run it.'''
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()


# Implementation of createBank method
def createBank(number=0):
    """Saves a bank with the speci!ed number of accounts.
    Used during testing."""
    # create an object for Bank class
    bank = Bank()
    # Iterate the loop
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
    bank.save("bank.dat")


# Creates a bank with the following names / PINS:
# Name1, 1000
# Name2, 1001
# Name3, 1002
# Name4, 1003
# Name5, 1004
createBank(5)
# call main function
5 / 31 / 22, 8: 50
PM
Page
13
of
18
main()
bank.py:
'''
File: bank.py
This module de!nes the SavingsAccount and Bank classes.
'''
import pickle


# Implementation of SavingsAccount class
class SavingsAccount(object):
    '''This class represents a savings account
    with the owner's name, PIN, and balance.'''

    RATE = 0.02

    # Implementation of __init__
    def __init__(self, name, pin, balance=0.0):
        self._name = name

    self._pin = pin
    self._balance = balance

    # Implementation of __str__ method
    def __str__(self):
        result = 'Name: ' + self._name + '\n'

    result += 'PIN: ' + self._pin + '\n'
    result += 'Balance: ' + str(self._balance)
    return result

    # Implementation of getBalance method
    def getBalance(self):
        return self._balance

    # Implementation of getName method
    def getName(self):
        return self._name

    # Implementation of getName method
    def getPin(self):
        return self._pin

    # Implementation of deposit method
    def deposit(self, amount):
        '''Deposits the given amount.'''

    self._balance += amount
    return self._balance

    # Implementation of withdraw method
    def withdraw(self, amount):

    # check amount is less than 0 or not
    if amount < 0:
        return 'Amount must be >= 0'
    elif self._balance < amount:
        return 'Insu#cient funds'
    else:
    self._balance -= amount
    return None

    # Implementation of computeInterest method
    def computeInterest(self):
        '''Computes, deposits, and returns the interest.'''

    # calculate interest
    interest = self._balance * SavingsAccount.RATE
    self.deposit(interest)
    return interest


# Implementation of Bank class
class Bank(object):
    '''This class represents a bank as a dictionary of
    accounts. An optional !le name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent !le storage.'''

    # Implementation of __init__
    def __init__(self, !leName = None):
        '''Creates a new dictionary to hold the accounts.
        If a !le name is provided, loads the accounts from
        a !le of pickled accounts.'''

    self._accounts = {}
    self.!leName = !leName
    # check !leName is not equal to None
    if !leName != None:
    # open the !le in read mode
    !leObj = open(!leName, 'rb')
    # Iterate the loop
    while True:
        try:
            account = pickle.load(!leObj)
        self.add(account)
        except EOFError:
        # close the !le
    5 / 31 / 22, 8: 50
    PM
    Page
    15
    of
    18
    !leObj.close()
    break

    # Implementation of add method
    def add(self, account):
        '''Inserts an account using its PIN as a key.'''

    self._accounts[account.getPin()] = account

    # Implementation of remove method
    def remove(self, pin):
        return self._accounts.pop(pin)

    # Implementation of get method
    def get(self, pin):
        return self._accounts.get(pin, None)

    # Implementation of computeInterest method
    def computeInterest(self):
        '''Computes interest for each account and
    returns the total.'''

    total = 0
    # Iterate the loop
    for account in self._accounts.values():
        total += account.computeInterest()
    return total

    # Implementation of __str__ method
    def __str__(self):
        '''Return the string rep of the entire bank.'''

    return '\n'.join(map(str, self._accounts.values()))

    # Implementation of save method
    def save(self, !leName = None):
        '''Saves pickled accounts to a !le. The parameter
    allows the user to change !le names.'''

    # check !leName is not equal to None
    if !leName != None:
        self.!leName = !leName
    elif self.!leName == None:
        return
    # open the !le in write mode
    !leObj = open(self.!leName, 'wb')

    # Iterate the loop
    for account in self._accounts.values():
        pickle.dump(account, !leObj)
        5 / 31 / 22, 8: 50
        PM
        Page
        16
        of
        18
        # close the !le
        !leObj.close()

        # Implementation of testBank method
        def testBank(self, number=0):
            '''Returns a bank with the speci!ed number of accounts and/or
    the accounts loaded from the speci!ed !le name.'''
            # create an object for Bank class
            bank = Bank()
            # Iterate the loop
            for i in xrange(number):
                bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
            return bank
