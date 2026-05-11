class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if self.__balance>0:
            self.__balance+=amount
            print("deposited successfuly")
        else:
            print("not deposited")
    def withdraw(self,amount):
        if self.__balance>0:
            self.__balance-=amount
            print("amount withdrawed successfuly")
        else:
            print("try again")
    def display(self):
        return self.__balance

b=bank(1000)
b.deposit(200)
b.withdraw(200)
print(b.display())

class config:
    def __init__(self):
        self.__setting={}
    def get(self,key):
        return self.__setting.get(key)
    def set(self,key,val):
        self.__setting[key]=val
    def delete(self,key):
        self.__setting.pop(key,None)
c=config()
c.set("name","indu")
c.set("age",18)
c.set("car","suzukkkki")
print(c.get("name"))
print(c.get("age"))
print(c.get("car"))


class bankaccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        self.__transcation_log=[]
    def deposit(self,amount):
        self.balance+=amount
        self.__transcation_log.append(f"deposit:{amount}")
    def withdraw(self,amount):
        self.balance-=amount
        self.__transcation_log.append(f"withdraw:{amount}")
    def transcation_history(self):
       return self.__transcation_log
b=bankaccount("indu",1000)
b.deposit(500)
b.withdraw(200)
b.deposit(100)
print(b.transcation_history())

class profile:
    def __init__(self,name,password):
        self.name=name
        self.__password=password
    def change_password(self,old,new):
        if old==self.__password:
            self.__password+=new
            return "password changed successfuly"
        else:
            return"old password is wrong! try again broo"
    def check_password(self,p):
        return p == self.__password
    

l=profile("indubiradar____","induuuu23")
print(l.change_password("induuuu23","ikb23"))
print(l.check_password("ik"))


