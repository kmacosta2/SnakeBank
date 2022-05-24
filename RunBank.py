import csv
from MenuLogic import MenuLogic
from Customer import Customer
from Checking import Checking
from Savings import Savings
from Credit import Credit
# Here in the RunBank file we're instantiating all the objects
def main():
    customers = {}
    try:
        with open("clientInfoFile.csv", newline='') as f:
            reader = csv.reader(f)
            header = next(reader) # first line is header too
            for row in reader:
                fn = row[0]
                ln = row[1]
                dob = row[2]
                id = int(row[3])
                addr = row[4]
                phone = row[5]
                checkAccNum = int(row[6])
                savAccNum = int(row[7])
                credAccNum = int(row[8])
                checkingBal = float(row[9])
                savingsBal = float(row[10])
                creditBal = float(row[11])
                creditMax = int(row[12])
                pw = row[13]
                email = row[14] #self,ID,  checkingAcc, savingsAcc, creditAcc,                                                        crdMax     pw, email,first,last,dob,addr,     phone
                cust = Customer(id, Checking(checkAccNum, checkingBal), Savings(savAccNum, savingsBal), Credit(credAccNum, creditBal, creditMax), pw, email, fn, ln, dob, addr, phone)
                fl = fn + ' ' + ln
                customers.update({fl: cust}) # adding to dict
    except FileNotFoundError as err:
        print('File wasn\'t found, please fix this before re-running \'SnakeBank\', thank you')
    else:
        MenuLogic.mainMenu(customers)
        print('Made it through...')

if __name__ == '__main__':
    main()
else:
    print('This is being imported to somewhere else')
