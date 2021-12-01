# Auther = Dhiraj Arya
# Github username = dhiraj80
# Email = dhirajkum00380@gmail.com

class BikeRent:
    def __init__(self,stock):
        self.stock = stock
        print('''
        1.Availale stock is -> 
        2.Rent a bike ->
        3.Exit
        ''')
    def stocks(self):
        print('Availale stock is -->',self.stock)

    def qty(self,q):
        if q<=0:
            print("Enter a correct value")
        elif q>self.stock:
            print("Enter a correct value(lessden qty)")
        else:
            print(f'Total bill is -> {q*500}')
            print('Availale stock is -> ',self.stock-q )
        

obj = BikeRent(100)

while True:
    user = int(input('Enter a value-> '))

    if user ==1:
        obj.stocks()
        print("")

    elif user ==2:
        qty = int(input('Enter a Qty (less then stock)-> '))
        obj.qty(qty)
        print("")
    else:
        break
