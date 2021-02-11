
class account:
    def __init__(self,name,number,balance):

        self.name   = name
        self.number = number
        self.balance= balance

    def accountInfo(self):
        print("name    :",self.name)
        print("Number  :",self.number)
        print("Balance :" ,self.balance)

    def withdraw(self,quantity):
        if(self.balance - quantity <0) :
           print("your balance is not enough !!")

        else :
            self.balance -=quantity
            print("new balance :",self.balance)


    def deposit(self,quantity):
        self.balance +=quantity
        print("new balance is :",self.balance)


account = account(" ismail Gorenek",1000,3000)
account.accountInfo()


account.deposit(5000)

