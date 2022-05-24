from Account import Account

class Checking(Account):
    def __init__(self, checkAccNum=0, checkingBal=0.0):
        super().__init__(checkAccNum, checkingBal)
                #self.checkingAccNum = checkAccNum
                #self.checkingBal = checkingBal
# Getters and Setters
#    def getCheckAccNum(self):
#        return self.checkingAccNum
#    def getCheckBal(self):
#        return self.checkingBal
#    def setCheckAccNum(self, checkingAccNum):
#        self.checkingAccNum = checkingAccNum
#    def setCheckBal(self, checkingBal):
#        self.checkingBal = checkingBal


#chck = Checking(123, 1245.67)
#print('accBal:', chck.get_accBal(), 'accNum:', chck.get_accNum())
#chck.set_accBal(2000.01)
#chck.set_accNum(4567)
#print('accBal:', chck.get_accBal(), 'accNum:', chck.get_accNum())