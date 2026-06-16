class BankAccount():
    def __init__(self,account_holder,balance,password):
        self.account_holder=account_holder
        self.balance=balance
        self.password=password
    
    def deposite(self,amount):
        if amount>=1:
            self.balance+=amount
            return f"{self.account_holder} thank you for depositing amount of ₹{amount} your current balance is:{self.balance}"
        else :
            return f"Invalid Amount entered"
    
    def withdraw(self,amount):
        if amount<=0:
            return f"Mazak Nhi Chalega, Zaada Masti Kari toh Bank Account Suspend Hojaega"
        
        elif amount>self.balance:
            return f"Beta,gareebi chal rahi hai, balance kam hai!"

        else:
            self.balance-=amount
            return f"{self.account_holder}, your withdrawal of {amount} is successfull, your current balance is:{self.balance}"
            

c1=BankAccount("Tester_Bro",2000,123456)

while True:
    print("Dear costumer",c1.account_holder,"BALANCE:₹",c1.balance)  
    choice=input("Enter W/w fro withdrawing money and D/d for depositing money or ENTER E/e FOR EXIT: ").strip().lower() 
    if choice == "w" or choice =="withdraw":
        amount=int(input("Enter The Amount You Want To WithDraw: "))
        passw=int(input("Enter Your Password:"))
        if passw==c1.password:
            print(c1.withdraw(amount))
        else:
            print("wrong password")

    elif choice == "d" or choice=="deposite":
        amount=int(input("Enter The Amount You Want To Deposite: "))
        passw=int(input("Enter Your Password:"))
        if passw==c1.password:
            print(c1.deposite(amount))
        else:
            print("wrong password")

    elif choice=="e":
        exit()
    else:
        print("wrong choice")