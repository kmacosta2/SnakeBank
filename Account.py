class Account:
    def __init__(self, accNum, accBal):
        self.accNum = accNum
        self.accBal = accBal

#   Getters and setters below    
    def get_accNum(self):
        return self.accNum
    def get_accBal(self):
        return self.accBal
    def set_accNum(self, accNum):
        self.accNum = accNum
    def set_accBal(self, accBal):
        self.accBal = accBal
#   Inquiring on the current balance of the account
    def inquireBal(self):
        return self.accBal
#   Deposit function for accounts
    def deposit(self, amount):
        amount = float(amount)
        self.set_accBal(round(self.accBal + amount, 2))
        print('\tNew Account balance:', self.accBal)

#   Withdraw funds from an account
#   Notify the MenuLogic that it was a successful withdrawal,
#   so it can then display in the menu that it happened
    def withdraw(self, amount, mode='regular'):
        remaining = self.accBal - (float(amount))
        if remaining >= 0:
            self.set_accBal(round(remaining, 2))
            print('\tNew Account balance:', self.accBal)
            if mode == 'pay' or mode == 'transfer':
                return True
        else:
            print('\tInsufficient funds')
            if mode == 'pay' or mode == 'transfer':
                return False
#   Pay funds to another Bank Customer from the signed-in Customer's account
    def pay(self, who, whichAcc, amount, customers):
        try:
            if customers[who]: # First checking for other customer's existence
                if self.withdraw(amount, 'pay'): # Then Checking to see if there are funds
                    if whichAcc == '0':
                        print('Other customer ',end='')
                        customers[who].getCheckingAcc().deposit(amount)
                    elif whichAcc == '1':
                        print('Other customer ',end='')
                        customers[who].getSavingsAcc().deposit(amount)
        except KeyError as err:
            print('\tInvalid Name, please try again')

#   Working strictly from the same customer's account; user can send funds one account to another.
    def transfer(self, customer, toAcc, amount):
        if self.withdraw(amount, 'transfer'): # Then Checking to see if there are funds
            if toAcc == '0':
                print('\tChecking')
                customer.getCheckingAcc().deposit(amount)
            elif toAcc == '1':
                print('\tSavings')
                customer.getSavingsAcc().deposit(amount)

