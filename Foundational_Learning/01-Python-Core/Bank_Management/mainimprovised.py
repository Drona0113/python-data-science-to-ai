import json
import random
import string
from pathlib import Path

class Bank:

    database = Path(__file__).parent / "data.json"
    data = []

    @classmethod
    def load_data(cls):
        try:
            if cls.database.exists():
                with open(cls.database, "r") as fs:
                    cls.data = json.load(fs)
            else:
                cls.data = []

        except (json.JSONDecodeError, OSError) as e:
            print(f"An exception occurred: {e}")
            cls.data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __account_generate(cls):

        while True:

            alpha = random.choices(string.ascii_letters,k=3)

            num = random.choices(string.digits,k=3)

            sp_char = random.choices("!@#$%^&*",k=1)

            account_id = alpha + num + sp_char

            random.shuffle(account_id)

            account_number = "".join(account_id)

            # Make sure account number is unique
            if not any(account["accountNo."] == account_number for account in cls.data):
                return account_number

    @classmethod
    def __find_account(cls, account_number, pin):

        for account in cls.data:

            if (account["accountNo."] == account_number and account["pin"] == pin):
                return account

        return None

    @classmethod
    def create_account(cls, name, age, email, pin):

        if not name.strip():
            return False, "Name cannot be empty."

        if age <= 0:
            return False, "Age must be greater than 0."

        if not email.strip():
            return False, "Email cannot be empty."

        if not pin.isdigit():
            return False, "PIN must contain only numbers."

        account_number = cls.__account_generate()

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": account_number,
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()

        return True, account_number

    @classmethod
    def deposit_money(cls, account_number, pin, amount):

        account = cls.__find_account(account_number,pin)

        if not account:
            return False, "Sorry, no such account exists."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "You cannot deposit more than 10,000."

        account["balance"] += amount

        cls.__update()

        return True, "Amount deposited successfully."


    @classmethod
    def withdraw_money(cls, account_number, pin, amount):

        account = cls.__find_account(account_number,pin)

        if not account:
            return False, "Sorry, no such account exists."

        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."

        if account["balance"] < amount:
            return False, "You cannot withdraw more than your balance."

        account["balance"] -= amount

        cls.__update()

        return True, "Amount withdrawn successfully."

    @classmethod
    def show_details(cls, account_number, pin):

        account = cls.__find_account(account_number,pin)

        if not account:
            return None

        return account

    @classmethod
    def update_details(cls,account_number,pin,name=None,email=None,new_pin=None):

        account = cls.__find_account(account_number,pin)

        if not account:
            return False, "Sorry, no such account exists."

        if name is not None and name.strip():
            account["name"] = name

        if email is not None and email.strip():
            account["email"] = email

        if new_pin is not None and new_pin != "":

            if not new_pin.isdigit():
                return False, "PIN must contain only numbers."

            account["pin"] = new_pin

        cls.__update()

        return True, "Your details have been updated successfully."


    @classmethod
    def delete_account(cls, account_number, pin):

        account = cls.__find_account(account_number,pin)

        if not account:
            return False, "Sorry, no such account exists."

        if account["balance"] > 0:
            return False, (
                "You cannot delete an account "
                "with remaining balance."
            )

        cls.data.remove(account)
        cls.__update()

        return True, "Your account has been deleted successfully."

Bank.load_data()

