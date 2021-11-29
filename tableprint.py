# Auther = Dhiraj Arya
# Github username = dhiraj80
# Email = dhirajkum00380@gmail.com
try:
    print("******welcome to dhiraj table ganerter******")
    #user se table pattarn input 
    tablepattarn = int(input("Enter '1' for only enter value table print and '2' for seriel vase table print --> "))

    #only enter value print table
    if tablepattarn==1:
        userinput = int(input('enter value for print table --> '))
        for num in range(1,11):
            print(f"{userinput} x {num} -> {userinput*num}")

    #serial vase table print
    elif tablepattarn==2:
        user = int(input('enter value for print table( 1-enter num) --> '))
        user = user+1
        for n in range(1,user):
            print("")
            for a in range(1,11):
                print(f"{n} x {a} -> {n*a}")

    else:
        exit()

except:
    print("############ thanks for vist ############")