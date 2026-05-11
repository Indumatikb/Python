'''
class bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance+=amount
        print(f"Deposited {amount}. New balance: {self.__balance}")


    def taking(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

        else:
            print("not enough balance!")




acc=bankaccount("acc134", 10000)
print("balance:",acc)
'''

class phone:
    def call_contact(self):
        print("call contacted")
    def take_picture(self):
        print("picture taken")


phone=phone()
phone.call_contact()
phone.take_picture()