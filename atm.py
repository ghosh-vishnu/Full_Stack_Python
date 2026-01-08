class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdraw Successfully withdrawal amount is",amount)
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print("Balance is ",self.balance)
acc=BankAccount("Vishnu",10000)
acc.deposit(5000)
acc.withdraw(9000)
acc.show_balance()
        
    
        
        
    