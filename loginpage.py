import sqlite3
import os.path

if not os.path.exists("loginfo.db"):
    conn = sqlite3.connect("loginfo.db")
    conn.execute("""
    create table Logindata(
        st_userid varchar(10),
        st_userpwd varchar(15)
    )
    """)
try:
    class LoginPanal:
        def __init__(self):
            print('welcome to dhiraj login panal.......')
            print("""
            1. LOGIN PANAL
            2. CREATE NEW ACCOUNT
            """)

        def login(self):
            print('\nwelcome to dhiraj login page.......')
            conn = sqlite3.connect("loginfo.db")
            self.userin = input('enter user name--> ')
            self.userpwd = input('enter password--> ')
            self.data = conn.execute('select * from Logindata')
            for self.d in self.data:
                self.us_id = self.d[0]
                self.us_pwd = self.d[1]
            if self.us_id in self.userin and self.us_pwd in self.userpwd:
                print('welcome to you are login sucesful..')
                print("*******************************************************")

            else:
                print("invilad userid and password")


        def createaccount(self):
            print("\nwelcome to create account.......")
            conn = sqlite3.connect("loginfo.db")
            self.userin = input('enter user name--> ')
            self.userpwd = input('enter password--> ')
            self.data = ("insert into Logindata VALUES (?,?)")
            self.d = (self.userin,self.userpwd)
            conn.execute(self.data,self.d)
            print('Account create sucessful---')
            print("*******************************************************")
            conn.commit()
            conn.close()


    runlogin = LoginPanal()

    while True:
        op = int(input("\nEnter chose opsstion--> "))

        if op==1:
            runlogin.login()

        elif op==2:
            runlogin.createaccount()

except:
    print("*******************************************************")
    exit()