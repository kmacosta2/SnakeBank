from Snake import Snake
from Savings import Savings
from Credit import Credit
from Checking import Checking
from LogStatements import LogStatements

class Customer(Snake):                                                                      # , checkStartBal=0, savStartBal=0, credStartBal=0
    def __init__(self, ID=0, checkingAcc=Checking(), savingsAcc=Savings(), creditAcc=Credit(), pw='', email='', first='', last='', dob='', addr='', phone=''):
        super().__init__(first, last, dob, addr, phone)
        self.id = ID
        self.checkingAcc = checkingAcc
        self.savingsAcc = savingsAcc
        self.creditAcc = creditAcc
        #self.checkStartBal = checkStartBal
        #self.savStartBal = savStartBal
        #self.credStartBal = credStartBal
        self.pw = pw
        self.email = email
        #self.logger = LogStatements()

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def getPassword(self):
        return self.pw
    def setPassword(self, pw):
        self.pw = pw

    #def getTransactions(self):
    #    return self.trasactions
    #def addTransaction(self, transAct):
    #    self.trasactions.append(transAct)
    
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

    #cust = Customer(80626162, Checking(123, 1245.67), Savings(980, 1122.12), Credit(565, 7878.34, 250, 180), 'password', 'something@gmail.com', 'kevin', 'ace', 'June 03 1990', 'University Ave', '(915)999-9932')
#print(cust.getAddress())
#cust.addTransaction('hey')
#cust.addTransaction('finally')
#print(cust.getTransactions()[1])
###########################################################################################
#                           Test cases for CHECKING
    #print('accBal:', cust.checkingAcc.get_accBal(), 'accNum:', cust.checkingAcc.get_accNum())
    #cust.checkingAcc.set_accBal(2000.01)
    #cust.checkingAcc.set_accNum(4567)
    #print('accBal:', cust.checkingAcc.get_accBal(), 'accNum:', cust.checkingAcc.get_accNum())
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
