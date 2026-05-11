class person:
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if 0<= new_age <= 120:
            self.__age=new_age
        else:
            print("invalid age")
p=person(18)
print(p.get_age())
p.set_age(23)
print(p.get_age())

class locker:
    def __init__(self,pin):
        self.__pin=pin
    def verify_pin(self,verify):
        if self.__pin==verify:
            return ("verified")
        else:
            return ("not verified")
l=locker(123)
print(l.verify_pin(123))
print(l.verify_pin(990))

class secert:
    def __init__(self):
        self.__hidden="i am secert"
s=secert()
print(s._secert__hidden)
