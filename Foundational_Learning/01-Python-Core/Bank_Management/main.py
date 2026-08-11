
import json
import random
import string
from pathlib import Path

class Bank:
    database=Path(__file__).parent/"data.json"
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())

        else:
            print("no such file exist")
    except Exception as e:
        print(f"an exception occurred as {e}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __account_generate(cls):
        alpha=random.choices(string.ascii_letters, k=3)
        num=random.choices(string.digits, k=3)
        sp_char=random.choices("!@#$%^&*", k=1)
        id=alpha+num+sp_char
        random.shuffle(id)
        return "".join(id)

    def Create_account(self):
        info={
            "name":input("tell your name : "),
            "age":int(input("tell your age : ")),
            "email":input("tell your email : "),
            "pin":int(input("tell your pin : ")),
            "accountNo.":self.__account_generate(),
            "balance":0,
        }
        for i in info:
            print(f"{i} :{info[i]}")
        print("please note down your account number for future reference")
        Bank.data.append(info)
        Bank.__update()


    def Deposit_money(self):
        accnumber=input("enter your account number : ")
        pin=int(input("enter your pin : "))
        

        userdata=[i for i in self.data if i["accountNo."]==accnumber and i["pin"]==pin]

        if userdata==False:
            print("sorry no such account exist")
        else:
            amount=int(input("enter amount you want to deposit : "))
            if amount>10000 or amount<0:
                print("sorry you can not deposit more than 10000 or less than 0")
            else:
                userdata[0]['balance']+=amount
                self.__update()
                print("Amount deposited succesfully")


    def Withdraw_money(self):
            accnumber=input("enter your account number : ")
            pin=int(input("enter your pin : "))
            
    
            userdata=[i for i in self.data if i["accountNo."]==accnumber and i["pin"]==pin]
    
            if userdata==False:
                print("sorry no such account exist")
            else:
                amount=int(input("enter amount you want to withdraw : "))
                if userdata[0]['balance']<amount:
                    print("sorry you can not withdraw more than your balance")
                else:
                    userdata[0]['balance']-=amount
                    self.__update()
                    print("Amount withdrawn succesfully")
    




user=Bank()
print("press 1 for creating an account")
print("press 2 for Depositing money in the bank")
print("press 3 for withdrawing money from the bank")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting the account")
check=int(input("enter your choice : "))
if check==1:
    user.Create_account()

if check==2:
    user.Deposit_money()

if check==3:
    user.Withdraw_money()