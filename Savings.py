from Account import Account

class Savings(Account):
    def __init__(self, savAccNum=0, savingsBal=0.0):
        super().__init__(savAccNum, savingsBal)
                #self.savAccNum = savAccNum   # a int
                #self.savingsBal = savingsBal # a double
    # Getters and Setters
    #def getSavAccNum(self):
    #    return self.savAccNum
    #def getSavingsBal(self):
    #    return self.savingsBal
    #def setSavAccNum(self, savAccNum):
    #    self.savAccNum = savAccNum
    #def setSavingsBal(self, savingsBal):
    #    self.savingsBal = savingsBal


#savs = Savings(123, 1245.67)
#print('accBal:', savs.get_accBal(), 'accNum:', savs.get_accNum())
#savs.set_accBal(2000.01)
#savs.set_accNum(4567)
#print('accBal:', savs.get_accBal(), 'accNum:', savs.get_accNum())