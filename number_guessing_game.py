# Auther = Dhiraj Arya
# Github username = dhiraj80
# Email = dhirajkum00380@gmail.com

import random
time = 11
#number = 53
number = random.randint(1,100)
#print(number)
print("*************    welcome to frist game project   *************")
n = 11
while n>0:
    #print("Your Time Lift --> ", time)
    userinput = int(input('Enter Guess Number --> '))

    if userinput<number :
        print("Plaese Enter Number Higest! ")
        print("Your Time Lift --> ",time-1)

    elif userinput>number :
        print("Plaese Enter Number Lower! ")
        print("Your Time Lift --> ",time-1)

    elif userinput==number :
        print("You Win! ")
        print("Number Is --> ",number)

    n = n-1
    time = time-1

print("----->    Thanks For Play     <------")
print("--> Auther = Dhiraj Arya <--")