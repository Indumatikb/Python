class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def from_string(cls,string):
        name, age = string.split("-")
        return cls(name, int(age))
p=person.from_string("indu-18")
print(p.name)
print(p.age)

#2nd ques
class logger:
    @staticmethod
    def log(msg,level):
        print(f" {level},{msg}")

logger.log("program started","info")
logger.log("program ended bro","techevent")

#3rd que
class counter:
    _instance=[]
    def __init__(self):
        self.count=0
        counter._instance.append(self)
    def increment(self):
        self.count+=1
    @classmethod
    def reset_all(cls):
        for instance in cls._instance:
            instance.count=0

counter1=counter()
counter2=counter()
counter3=counter()

counter1.increment()
counter1.increment()
counter1.increment()

counter2.increment()
counter2.increment()

counter3.increment()

print(counter1.count)
print(counter2.count)
print(counter3.count)

counter.reset_all()
print(counter1.count)
print(counter2.count)
print(counter3.count)

#4th que
class eventconfig:
    def __init__(self,name,date,fee):
        self.name=name
        self.date=date
        self.fee=fee
    @classmethod
    def from_dict(cls,data):
        return cls(data['name'],data['date'],data['fee'])
    @staticmethod
    def validate_fee(fee):
        return fee>=0 and fee<=100000
e1=eventconfig.from_dict({'name':'conference','date':'22-3-2026','fee':500})
print(f"name:{e1.name}, date:{e1.date}, fee:{e1.fee}")
print(eventconfig.validate_fee(100))
print(eventconfig.validate_fee(-190))