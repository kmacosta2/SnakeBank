from Account import Account

class Credit(Account):
    def __init__(self, credAccNum=0, creditBal=0.0, credMax = 0):
        super().__init__(credAccNum, creditBal)
        self.creditMax = credMax          # unique to credit: creditMax
    
    # Getters and Setters
    def getCreditMax(self):
        return self.creditMax
    def setCredMax(self, creditMax):
        self.creditMax = creditMax

#cred = Credit(123, 1245.67, 2000)
#print('accBal:', cred.get_accBal(), 'accNum:', cred.get_accNum())
#print('credMax:', cred.getCreditMax())
#cred.set_accBal(2000.01)
#cred.set_accNum(4567)
#cred.setCredMax(3000)
#print('accBal:', cred.get_accBal(), 'accNum:', cred.get_accNum())
#print('credMax:', cred.getCreditMax())
