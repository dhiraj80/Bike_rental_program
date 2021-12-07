import time
pin = 1234

statment = '''        JOHN JONES                                  Statement period  Account No.
        1643 DUNDAS ST W APT 27                 2003-10-09 to 2003-11-08  00005- 
        TORONTO ON M6K 1V2                                            123-456-7

  Date               Description            Ref.Withdrawals  Deposits   Balance
2003-10-08 Previous balance                                                0.55
2003-10-14 Payroll Deposit - HOTEL                             694.81     695.36
2003-10-14 Web Bill Payment - MASTERCARD    9685    200.00                495.36
2003-10-24 Interac Refund - ELECTRONICS     1975                 2.99     43.53
2003-10-27 Telephone Bill Payment - VISA    2475      6.77                36.76
2003-10-28 Payroll Deposit - HOTEL                             694.81     731.57
2003-10-30 Web Funds Transfer - From SAVINGS2620               50.00      781.57
2003-11-03 Pre-Auth. Payment - INSURANCE              33.55               748.02
2003-11-03 Cheque No. - 409                         100.00                648.02
2003-11-06 Mortgage Payment                         710.49                -62.47

                       "" Totals ""                 1,515.63   1,442.61
'''
def checkpin():
    user = input("Enter atm pin --> ")
    if int(user) == pin:
           pass 
    elif user=='':
        print("pin not vaild")
        exit()
    else:
        print("Worang atm pin ---  ")
        exit()

print("\t\t\t\t\twelcome to abc bank\t\t\t\t\t")
print("please enter card and continue--")
time.sleep(2)
print("proscesing........\n")
time.sleep(4)

try:
    print('\nplease choose options---\n1. Account statement \n2. Deposit money \n3. Withdral money \n4. exit')
    while True:
        op = int(input("  \nEnter --> "))
    ####################################################################################
        if op==1:
            checkpin()
            print(statment)

    ####################################################################################
        elif op==2:
            dp = input('Enter amount --> ')
            checkpin()
            print("________Amount Deposit Suceesful________")

    ####################################################################################
        elif op==3:
            wd = input("Enter Withdral Amount --> ")
            cnwd = input("Confrom Withdral Amount --> ")
            if wd == cnwd:
                checkpin()
                print("________Amount Withdral Suceesful________")
            else:
                print("Amount not Match!!")
            
    ###################################################################################

        else:
            exit()

except:
    exit()
