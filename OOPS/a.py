class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def calculate_avg(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        return avg
    
    def display(self):
        avg=self.calculate_avg()

        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=55:
            return "C"
        else:
            return "fail"
        


s=student("indu",[50,80,90])
print("average=",s.calculate_avg())
print("grade:",s.display())

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
a=rectangle(10,2)
print(a.area())
p=rectangle(10,2)
print(p.perimeter())


class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def apply_discount(self,percent):
        discount=(self.price*percent)/100
        new_price=self.price-discount
        return new_price

b=book("wings_of_fire","apj_abdul_kalam",10000)
print("after discount:",b.apply_discount(10))

class car:
    total_cars=0
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        car.total_cars+=1

c1=car("maruti_suzuki","2026")
c2=car("maruti_suzuki","2025")
print(car.total_cars)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return self.name,self.age
    
class emplyoee(person):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        return self.name, self.age, self.salary
    
c=emplyoee("indu",18,121000)
print(c.display())

class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            return "you can't add negative money"
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            return "insufficient amount"
        
    def get_balance(self):
        return self.__balance
    
b=bank(1000)
b.deposit(1000)
b.withdraw(200)
print("balance:",b.get_balance())

class products:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
    

p=products("laptops",1220000)
print(p.__repr__())
print(p.__str__())

class engine:
    def __init__(self,engine_start):
        self.engine_start=engine_start

    def start_engine(self):
        return "engine started"

class car:
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=engine

    def start_car(self):
        return self.engine.start_engine()

e=engine("v8")
c=car("suzuki",e)
print(c.start_car())

class number:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __add__(self):
        return ({self.n1+self.n2})
        
n=number(10,20)
print(n.__add__())

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

