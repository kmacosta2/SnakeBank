from time import perf_counter
from datetime import datetime

class LogStatements():
    def __init__(self):
        self.t1_start = perf_counter() # measure duration of session
        self.transactions = []

    def terminateSess(self):
        t2_end = perf_counter()
        print('Session duration:', t2_end-(self.t1_start))
        now = datetime.now()
        dt_frmtted = now.strftime("%m/%d/%Y %H:%M:%S")
        print("data and time =", dt_frmtted)
        # gen statement/txt file here below using self.transactions & write them all..
    
    def addTransaction(self, transAct):
        self.transactions = transAct
#ls = LogStatements()
#ls.terminateSess()