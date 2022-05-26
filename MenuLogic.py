import time
# This is purely menu logic, this is never instantiated so, "review OOP in python" in order to use decorators
class MenuLogic:
    def mainMenu(customers):
        quit = False
        print('\nWelcome to the Snake Bank!')
        while not quit:
            response = input("\tAre you an individual(0) or a manager(1)? ")
            if response == '0':
                result = input("\tHello, are you a returning customer? (y, n, or q(quit)) ")
                if result.lower() == 'y':
                    #name = input("\tFirst and last name (space separated): ")
                    #name = name.lower()
                    name = 'pinocchio disney'
                    try:
                        if customers[name]:
                            #print('congrats, you exist')
                            #pw = input("\tpassword: ")
                            pw = 'Disney*Pinocchio!987'
                            if customers[name].getPassword() == pw:
                                MenuLogic.customerMenu(customers, name)
                                break
                            else:
                                print('\tWrong pw')
                                time.sleep(1) 
                    except KeyError as err:
                        print('\tInvalid information, please try again')
                        time.sleep(1)
                elif result == 'n':
                    print('Alright in order to create an account please provide first & last name, password to get started\n\t\tat the moment we aren\'t accepting any new applicants, sorry')
            elif response == '1':
                MenuLogic.managerMenu(customers)
                break

# This function contains the welcome screen as well as the "Deposit", "Inquire", & "Withdraw" basic services.
    def customerMenu(customers, name):
        print('\n\tWelcome back', customers[name].getfName(), customers[name].getlName())
        custom = customers[name]
        service = ''
        while service != '0':
            service = input("\tInquire Balance: 1\n\tDeposit: 2\n\tWithdraw: 3\n\tPay Someone: 4\n\tTransfer: 5\n\tGenerate Statement: 6\n\tQuit: 0\n\t")
            if service != '0':
                if service == '1': # Customers can only "inquire" about Credit
                    accType = input("\tAccount Type: Checking: 0\tSaving: 1\tCredit: 2\n\t")
                else:
                    accType = input("\tAccount Type: Checking: 0\tSaving: 1\n\t")
            if service == '1':  # Inquire
                if accType == '0':
                    print('\n\tChecking Balance:', custom.getCheckingAcc().inquireBal())
                    custom.addTransaction(0, whichAcc=0)             
                elif accType == '1':
                    print('\n\tSavings Balance:', custom.getSavingsAcc().inquireBal())
                    custom.addTransaction(0, whichAcc=1)
                elif accType == '2':
                    print('\n\tCredit Balance:', custom.getCreditAcc().inquireBal())
                    custom.addTransaction(0, whichAcc=2)

            elif service == '2':  # Deposit
                amount = input("\tDeposit amount: ")
                if accType == '0':
                    print('\n\tChecking deposit of', amount)
                    custom.getCheckingAcc().deposit(amount)
                    custom.addTransaction(1, whichAcc=0, amount=amount)
                elif accType == '1':
                    print('\n\tSavings deposit of', amount)
                    custom.getSavingsAcc().deposit(amount)
                    custom.addTransaction(1, whichAcc=1, amount=amount)
                elif accType == '2':
                    print('\n\tCredit deposit unavailable')

            elif service == '3':  # Withdraw
                amount = input("\tWithdraw amount: ")
                if accType == '0':
                    print('\n\tChecking withdraw of', amount)
                    custom.getCheckingAcc().withdraw(amount)
                    custom.addTransaction(2, whichAcc=0, amount=amount)
                elif accType == '1':
                    print('\n\tSavings withdraw of', amount)
                    custom.getSavingsAcc().withdraw(amount)
                    custom.addTransaction(2, whichAcc=1, amount=amount)
                elif accType == '2':
                    print('\n\tCredit withdraw unavailable')

            elif service == '4' or service == '5':  # Pay Someone And Transfer
                MenuLogic.custAdvServices(customers, custom, accType, service)
            elif service == '6':
                custom.genBankStatements()
        else:
            n = customers[name].getfName() + ' ' + customers[name].getlName()
            print(f'Goodbye {n}\nThank you, come again!')

    # The more complex services provided here so as to avoid too much cluttered code in one method
    # Delivers "Pay Someone" & "Transfer from another account type"
    def custAdvServices(customers, customer, accType, service):
        if service == '4': # Pay Someone
            who = input("To who would you like to send the payment to?")
            whichAcc = input("To which of their accounts?(Checking: 0 Savings: 1)\n")
            amount = input("How much would you like to pay them?\n")
            if accType == '0':
                print('\n\tChecking Balance:', customer.getCheckingAcc().pay(who, whichAcc, amount, customers))
                customer.addTransaction(3, whichAcc=0, amount=amount, who=who, otherAcc=whichAcc)
            if accType == '1':
                print('\n\tSavings Balance:', customer.getSavingsAcc().pay(who, whichAcc, amount, customers))
                customer.addTransaction(3, whichAcc=1, amount=amount, who=who, otherAcc=whichAcc)

        elif service == '5': # Transfer
            toAcc = input("To what other account? ")
            amount = input("How much would you like to transfer? ")
            if accType == '0':
                print('\n\tChecking Balance:', customer.getCheckingAcc().transfer(customer, toAcc, amount))
                customer.addTransaction(4, whichAcc=0, amount=amount, otherAcc=toAcc)
            if accType == '1':
                print('\n\tChecking Balance:', customer.getSavingsAcc().transfer(customer, toAcc, amount))
                customer.addTransaction(4, whichAcc=1, amount=amount, otherAcc=toAcc)

    def managerMenu(customers):
        print('\tManager menu')
        time.sleep(1)
