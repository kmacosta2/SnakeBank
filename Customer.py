from Snake import Snake
from Savings import Savings
from Credit import Credit
from Checking import Checking
from LogStatements import LogStatements
from datetime import datetime

class Customer(Snake):
    def __init__(self, ID=0, checkingAcc=Checking(), savingsAcc=Savings(), creditAcc=Credit(), pw='', email='', first='', last='', dob='', addr='', phone=''):
        super().__init__(first, last, dob, addr, phone)
        self.id = ID
        self.checkingAcc = checkingAcc
        self.savingsAcc = savingsAcc
        self.creditAcc = creditAcc
        self.pw = pw
        self.email = email
        #self.logger = LogStatements()
        self.transactionStatements = []

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def getPassword(self):
        return self.pw
    def setPassword(self, pw):
        self.pw = pw
# Trasactions are intended to be added to everytime a customer performs an activity 
    def getTransactions(self):
        return self.transactionStatements
    
    def addTransaction(self, which='', whichAcc='', amount=0.0, who='', otherAcc=''):
        # which: (Inquire) 0, (deposit) 1, (withdraw) 2, (pay) 3, (transfer) 4
        # whichAcc: (Checking) 0, (Savings) 1, (Credit) 2
        # otherAcc: Checking 0, Savings 1, Credit 2 <--For pay, refers to other person's acc. For Transfer, refers to same person, 2nd account
        whichAcc = self.getCurrAccType(whichAcc)
        otherAcc = self.getCurrAccType(otherAcc)
        if which == 0: # Inquired
            self.transactionStatements.append(f'From {whichAcc} Inquired Balance')
        if which == 1: # Deposit
            self.transactionStatements.append(f'From {whichAcc} Deposited {amount}')
        if which == 2: # Withdraw
            self.transactionStatements.append(f'From {whichAcc} Withdrew {amount}')
        if which == 3: # Pay
            self.transactionStatements.append(f'Paid {who}\'s {otherAcc} account ${amount} from {whichAcc}')
        if which == 4: # Transfer
            self.transactionStatements.append(f'Transferred {amount} from {whichAcc} to {otherAcc}')
        print('\n\tthe most recent transaction statements:', self.transactionStatements)

    def getID(self):
        return self.id
    def setID(self, ID):
        self.id = ID
    def getCheckingAcc(self):
        return self.checkingAcc
    def setCheckingAcc(self, checkingAcc):
        self.checkingAcc = checkingAcc
    def getSavingsAcc(self):
        return self.savingsAcc
    def setSavingsAcc(self, savingsAcc):
        self.savingsAcc = savingsAcc
    def getCreditAcc(self):
        return self.creditAcc
    def setCreditAcc(self, creditAcc):
        self.creditAcc = creditAcc
#   This function returns the accoun type from which this instance is being accesed from (polymorphism) in a string
#   whichAcc: (Checking) 0, (Savings) 1, (Credit) 2
    def getCurrAccType(self, num):
        if num == 0:
            return 'Checking'
        elif num == 1:
            return 'Saving'
        elif num == 2:
            return 'Credit'

#   Here I'll create a new .txt file in which I'll fill with all the actions the customer has performed during their last session.
    def genBankStatements(self):
        t = self.transactionStatements
        now = datetime.now()
        dt_frmtted = now.strftime("%m/%d/%Y %H:%M:%S")
        try:
            with open(f"/Users/kevinacosta/VisualStudioProjects/{self.getfName()}{self.getlName()}Statement.txt", 'w') as f:
                f.write("\t\tSnake Bank\n")
                f.write("------------------------------------------\n")
                f.write(f"{dt_frmtted}\nCustomer: {self.getfName()} {self.getlName()}\n")
                for i, line in enumerate(t):
                    f.write('\t' + str(i) + ' ' + line + '\n')
            print('An attempt at printing:\n', self.getTransactions())
        except FileNotFoundError as err:
            print('File wasn\'t found, please fix this before re-running \'SnakeBank\', thank you')

#cust = Customer(80626162, Checking(123, 1245.67), Savings(980, 1122.12), Credit(565, 7878.34, 250), 'password', 'something@gmail.com', 'kevin', 'ace', 'June 03 1990', 'University Ave', '(915)999-9932')
#print(cust.getAddress())
#cust.addTransaction('hey')
#cust.addTransaction('finally')
#print(cust.getTransactions()[1])
#cust.genBankStatements()
###########################################################################################
#                           Test cases for CHECKING
#           print('accBal:', cust.getCheckingAcc().inquireBal(), 'accNum:', cust.getCheckingAcc().get_accNum())
#           cust.checkingAcc.set_accBal(2000.01)
#           cust.checkingAcc.set_accNum(4567)
#           print('accBal:', cust.getCheckingAcc().inquireBal(), 'accNum:', cust.getCheckingAcc().get_accNum())
######################################################################################## 
#                           Test cases for SAVINGS
    #print('accBal:', cust.savingsAcc.get_accBal(), 'accNum:', cust.savingsAcc.get_accNum())
    #cust.savingsAcc.set_accBal(2000.01)
    #cust.savingsAcc.set_accNum(4567)
    #print('accBal:', cust.savingsAcc.get_accBal(), 'accNum:', cust.savingsAcc.get_accNum())
######################################################################################## 
#                           Test cases for CREDIT
    #print('accBal:', cust.creditAcc.get_accBal(), 'accNum:', cust.creditAcc.get_accNum())
    #print('credMax:', cust.creditAcc.getCreditMax(), 'credScore:', cust.creditAcc.getCreditScore())
    #cust.creditAcc.set_accBal(2000.01)
    #cust.creditAcc.set_accNum(4567)
    #cust.creditAcc.setCreditScore(300)
    #cust.creditAcc.setCredMax(333)
    #print('accBal:', cust.creditAcc.get_accBal(), 'accNum:', cust.creditAcc.get_accNum())
    #print('credMax:', cust.creditAcc.getCreditMax(), 'credScore:', cust.creditAcc.getCreditScore())
