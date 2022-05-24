import time
#
# This is purely menu logic, this is never instantiated so, "review OOP in python" in order to use decorators
#                                                         here or something similar to that.
class MenuLogic:
    def mainMenu(customers):
        quit = False
        print('\nWelcome to the Snake Bank!')
        while not quit:
            response = input("\tAre you an individual(0) or a manager(1)? ")
            if response == '0':
                result = input("\tHello, are you a returning customer? (y, n, or q(quit)) ")
                if result.lower() == 'y':
                    name = input("\tFirst and last name (space separated): ")
                    name = name.lower()
                    try:    
                        if customers[name]:
                            #print('congrats, you exist')
                            pw = input("\tpassword: ")
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

    def customerMenu(customers, name):
        print('\tWelcome back', customers[name].getfName(), customers[name].getlName())

    def managerMenu(customers):
        print('\tmanager menu')
        time.sleep(1)
