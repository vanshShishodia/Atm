class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin = pin

    def check_balance(self):
        print("your balance is 50,000")
    
    def withdrawl(self,amount):
        newamount=50000-amount
        print("you have withdrown amount "+str(amount)+". Your remaing balance is "+str(newamount))

def main():
    card_number=input('enter your card number:')
    pin_number=input('wnter your pin:')
    new_user=Atm(card_number,pin_number)
    print("choose your activity")
    print("1.balance enquiry 2.Withdrawl")
    activity=int(input("enter activity number:"))

    if(activity==1):
        new_user.check_balance()

    elif(activity==2):
        amount=int(input("enter the amount:"))
        new_user.withdrawl(amount)
    
    else:
        print("enter a vaild number:")

main()
        
