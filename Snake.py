# Like a 'Person' object, but with snakes as customers

class Snake:
    def __init__(self, first, last, dob, addr, phone):
        self.firstN = first
        self.lastN = last
        self.dob = dob
        self.addr = addr
        self.phone = phone
    # Getters and Setters
    def getfName(self):
        return self.firstN
    def getlName(self):
        return self.lastN
    def getDOB(self):
        return self.dob
    def getAddress(self):
        return self.addr
    def getPhone(self):
        return self.phone
    def setfName(self, first):
        self.firstN = first
    def setlName(self, last):
        self.lastN = last
    def setDOB(self, dob):
        self.dob = dob
    def setAddress(self, addr):
        self.addr = addr
    def setPhone(self, phone):
        self.phone = phone

#hiss = Snake()
#hiss.setfName('tom')
#hiss.setlName('slither')
#hiss.setDOB('June someday 1900')
#hiss.setAddress('University Ave.')
#hiss.setPhone('(915)999-9999')
#print(hiss.getfName())
#print(hiss.getAddress())
#print(hiss.getPhone())

# MISSING TO ADD: PasswordNotFoundException <-- Or An "ERROR Handler" class?