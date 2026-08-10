
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