class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"student_name:{self.name}, student_marks:{self.marks}")

s1=student("indu",9.15)
s1.display()
s2=student("sindhu",9)
s2.display()

class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def accelerate(self):
        print(f"car_brand:{self.brand}, car_speed:{self.speed}")

c1=car("suzuki",180)
c1.accelerate()


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculated_area(self):
        return self.length*self.breadth
    def calculated_perimeter(self):
        return 2+self.length*self.breadth
    
a=rectangle(12,4)
print(a.calculated_area())
print(a.calculated_perimeter())


class bank_account:
    def __init__(self,balance=0):
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("deposited", amount)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("withdrawed_amount=",amount)

    def check_balance(self):
        print("current_balance=", self.balance)

acc=bank_account(1000)
acc.deposit(500)
acc.withdraw(400)
acc.check_balance()


class employee:
    def __init__(self,name, monthly_salary):
        self.name=name
        self.monthly_salary=monthly_salary

    def yearly_salary(self):
        return 12*self.monthly_salary
    

emp=employee("indu",200000)
print(emp.yearly_salary())

class book:
    def __init__(self,title,availability=True):
        self.title=title
        self.availability=availability

    def check_availiablity(self):
        if self.availability:
            print(self.title, "is available")
        else:
            print(self.title,"is not available")

b=book("python_basics",True)
c=book("indu",False)
b.check_availiablity()
c.check_availiablity()

class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("name:",self.name)

class student(person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks

    def display_nm(self):
        print("student_name:",self.name)
        print("student_marks:",self.marks)


s=student("indu",9.15)
s.display()
s.display_nm()
    


class bank:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount
b=bank(82)
print(b.get_balance())
b.set_balance(3222)
print(b.get_balance())


class student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if new_marks>18:
            self.__marks=new_marks

s=student(3)
print(s.get_marks())
s.set_marks(35)
print(s.get_marks())  

class temperature:
    def __init__(self,celcius):
        self.__celcius=celcius
    def to_farenheit(self):
        return (self.__celcius*1.8)+32
    def  to_kelvin(self):
        return self.__celcius+273
    
t=temperature(25)
print(t.to_farenheit())
print(t.to_kelvin())

class mobile:
    def __init__(self,battery):
        self.__battery=battery
    def charge(self,amount):
        self.__battery+=amount
        if self.__battery>100:
            self.batery__=100
    def use(self,amount):
        self.__battery-=amount
        if self.__battery<0:
            self.__battery=0
    def get_battery(self):
        return self.__battery
    
m=mobile(50)
m.charge(30)
m.use(20)
print(m.get_battery())

class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("can't add your amount")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("amount not available")
    def get_balance(self):
        return self.__balance
        

b=bank(1000)
b.deposit(500)
b.withdraw(500)
print(b.get_balance())


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"name:{self.name}, marks:{self.marks}")


s=student("indumati",9.15)
s.display()

        
class car:
    def __init__(self,car_name):
        self.car_name=car_name
    def display(self):
        print(f"car={self.car_name}")
c1=car("SUZUKI")
c1.display()
c2=car("BMW")
c2.display()
c3=car("HONDA")
c3.display()


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculated_grade(self):
        if self.marks>=90:
            return"A+"
        elif self.marks>=75:
            return"B"
        elif self.marks>=60:
            return"C"
        elif self.marks>=40:
            return"D"
        else:
            return "fail"

s=student("indumati",9)
print(s.calculated_grade())
s2=student("sindhu",90)
print(s2.calculated_grade())
s3=student("sindhu",55)
print(s3.calculated_grade())


class engine:
    def __init__(self,engine):
        self.engine=engine
    def start_engine(self):
        return f" {self.engine} is starting"
e=engine("car")
print(e.start_engine())

class area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculated_area(self):
        return self.length*self.breadth

r=area(10,3)
print(r.calculated_area()) 

class perimeter:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def calculated_perimeter(self):
        return 2*(self.breadth+self.length)
    
p=perimeter(2,3)
print(p.calculated_perimeter())


class employee:
    def __init__(self,salary):
        self.salary=salary
    def increment_salary(self):
        ip=int(input("enter increment percentange:"))
        self.salary=self.salary+(ip/100*self.salary)
        return self.salary

e=employee(50000)
new_salary=(e.increment_salary())
print(new_salary)

class student:
    count=0
    def __init__(self,name):
        self.name=name
        student.count+=1
s1=student("indu")
s2=student("sindhu")
s3=student("llilly")


print(student.count)

class student:
    @staticmethod
    def validate_age(age):
        if age>=5 and age<=100:
            return True
        else:
            return False
        
print(student.validate_age(90))
print(student.validate_age(2))

class Employee:
    @staticmethod
    def validate_salary(salary):
        return salary>0
    
print(Employee.validate_salary(50000))
    
print(Employee.validate_salary(-50000))

class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price
class customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def buy_product(self,product):
        if self.balance>=product.price:
            self.balance=self.balance-product.price
            print(f"{self.name} had bought {product.name}")
            print(f"remaining balance is {self.balance}")
        else:
            print("insufficient amount")


p1 = Product("Laptop",1250000)

c1 = customer("Ram", 2000000)


c1.buy_product(p1)

class movie:
    def __init__(self,name):
        self.name=name
    
class seat:
    def __init__(self,seat_no):
        self.seat_no=seat_no
        self.booked=False

class customer:
    def __init__(self,name):
        self.name=name

class booking:
    def book_ticket(self,customer,movie,seat):
        if seat.booked==False:
            seat.booked=True
            print(f"{customer.name} booked seat {seat.seat_no} for {movie.name}")
        else:
            print("oh! sorry try next slot")

m1=movie("love-mocktail")
s1=seat("a1")
c1=customer("indumati")
b1=booking()
b1.book_ticket(c1,m1,s1)

class SmartDevice:

    def __init__(self, name):

        self.name = name
        self.status = False


    def turn_on(self):

        self.status = True

        print(f"{self.name} turned ON")


    def turn_off(self):

        self.status = False

        print(f"{self.name} turned OFF")



class Light(SmartDevice):

    def set_brightness(self, level):

        print(f"Brightness set to {level}")



class Fan(SmartDevice):

    def set_speed(self, speed):

        print(f"Fan speed set to {speed}")



class AC(SmartDevice):

    def set_temperature(self, temp):

        print(f"Temperature set to {temp}")



l1 = Light("Bedroom Light")

f1 = Fan("Hall Fan")

a1 = AC("Living Room AC")


l1.turn_on()

l1.set_brightness(80)

f1.turn_on()

f1.set_speed(3)

a1.turn_on()

a1.set_temperature(22)

#abstacction method questions

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return 2*(self.length+self.breadth)

c1=circle(5)
r1=rectangle(10,4)
print(c1.area())
print(r1.area())

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("car is starting")

    def stop(self):
        print("car is stopping")

class bike(vehicle):
    def start(self):
        print("bike is starting")

    def stop(self):
        print("bike is stopping")

c1=car()
b1=car()
print(c1.start())
print(b1.stop())

from abc import ABC,abstractmethod
class parents(ABC):
    @abstractmethod
    def job(self):
        pass

class mom(parents):
    def job(self):
        print("mom is software engineer")

class dad(parents):
    def job(self):
        print("dad is farmer")

m1=mom()
d1=dad()
print(m1.job())
print(d1.job())

from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print("payment done by UPI")
class card(payment):
    def pay(self):
        print("payment is done by card")

u1=UPI()
c1=card()
print(u1.pay())
print(c1.pay())

from abc import ABC,abstractmethod
class delivary(ABC):
    @abstractmethod
    def deliver(delivary):
        pass

class food_delivary(delivary):
    def deliver(self):
        print("food will be delivered soon")

class package_delivary(delivary):
    def deliver(self):
        print("package delivary will happen soon")

f=food_delivary()
p=package_delivary()
print(f.deliver())
print(p.deliver()) 

from abc import ABC,abstractmethod
class authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class passwordauth(authentication):
    def authenticate(self):
        return "user authenticated password"
    
class otpauth(authentication):
    def authenticate(self):
        return "user authenticated otp"
    

p=passwordauth()
o=otpauth()
print(p.authenticate())
print(o.authenticate())

from abc import ABC,abstractmethod
class cloud_storage(ABC):
    @abstractmethod
    def upload(self):
        pass
    @abstractmethod
    def download(self):
        pass

class google_drive(cloud_storage):
    def upload(self):
        return "file uploaded to googledrive"
    def download(self):
        return "file downloaded"
    
class drobox(cloud_storage):
    def upload(self):
        return "file uploade to dropbox"
    def download(self):
        return "file downloaded"
    

g=google_drive()
print(g.upload())
print(g.download())

class animal:
    def sound(animal):
        return "..."

class dog(animal):
    def sound(animal):
        return "boww!"
    
class cat(animal):
    def sound(animal):
        return "meoww!"
    
a=dog()
b=cat()
print(a.sound())
print(b.sound())

class credit_card():
    def payment(credit_card):
        return "..."
    
class UPI(credit_card):
    def payment(credit_card):
        return "payment done by UPI"

class cash(credit_card):
    def payment(credit_card):
        return "payment done by cash"
    
a=UPI()
b=cash()
print(a.payment())
print(b.payment())

class apps:
    def notification(apps):
        return "..."
    
class email:
    def notification(apps):
        return "email pushes notification"
    
class sms:
    def notification(apps):
        return "sms pushes notification"

class push:
    def notification(apps):
        return "push pushes notification"
    
a=email()
b=sms()
c=push()
print(a.notification())
print(b.notification())
print(c.notification())

class shape:
    def area(shape):
        return "area"
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    
a=circle(4)
print(a.area())

b=square(4)
print(b.area())

class parser:
    def parse(self,data):
        print("parsing data")

class JSONParser(parser):
    def parse(self, data):
        print(f"JSONParsering data: {data}")

class XMLParser(parser):
    def parse(self,data):
        print(f"XMLParsering data: {data}")

class CSVPParser(parser):
    def parse(self,data):
        print(f"CVPParsering data: {data}")

parsers=[
    JSONParser(),
    XMLParser(),
    CSVPParser()
]

for p in parsers:
    p.parse("sample data")


class car:
    def start(self):
        return "car is starting"
    
class bike:
    def start(self):
        return "bike is starting"
    
class cycle:
    def start(self):
        return "cycle is strating"
    
def start_vehicle(vehicle):
    print(vehicle.start())


c=car()
b=bike()
cy=cycle()
print(c.start())
print(b.start())
print(cy.start())

class numbers:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __add__(self):
        return self.n1+self.n2
    
a=numbers(9,1)
print(a.__add__())

class numbers:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __sub__(self):
        return self.n2-self.n1

s=numbers(9,1)
print(s.__sub__())

class plugin:
    def run(self):
        print("running")

class audioplugin(plugin):
    def run(self):
        return "audioplugin is running"

class imageplugin(plugin):
    def run(self):
        return "impageplugin is running"

class videoplugin(plugin):
    def run(self):
        return "videoplugin is running"
    
class pluginmanager:
    def start_plugin(self,plugin):
        print(plugin.run())

manager=pluginmanager()
a=audioplugin()
b=imageplugin()
c=videoplugin()
print(manager.start_plugin(a))
print(manager.start_plugin(b))
print(manager.start_plugin(c))

class animal:
    def sound(self):
        return "..."

class dog(animal):
    def sound(self):
        return "dog is barking bow bow"

class cat(animal):
    def sound(self):
        return "cat does meow meow"

d=dog()
c=cat()
print(a.sound())
print(c.sound())


    


