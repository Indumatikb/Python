class dog:
    pass
d=dog()
print(type(d))
print(isinstance(d, dog))

#1st que
class rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length

r=rectangle(10,2)
print(r.area())
        
#2 que
class book:
    def __init__(self,author,title,pages=100):
        self.author=author
        self.title=title
        self.pages=pages
    def display(self):
        return self.author,self.title,self.pages
b=book("abdul kalam","wings of fire")
print(b.display())

#3rd que
class temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    def farenheit(self):
        return (self.celcius*9/5)+32
t=temperature(10)
print(t.farenheit())

class mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.is_on=False
    def power(self):
        self.is_on=not self.is_on
        state= "ON" if self.is_on else "OFF"
        return f"{self.model} {self.price} is in state{state}"
m=mobile("samsung","s24",250000)
m1=mobile("iphone12","promax",122300)
print(m.power()) 
print(m1.power())

class age:
    def __init__(self,value):
        if not isinstance(value,int):
            raise TypeError("bro age must be in integer")
        if value<0 or value>150:
            raise ValueError(f"bro age {value} is not realistic")

try:
    a = age(-5)
except ValueError as e:
    print(e)

class goodteam:
    def __init__(self,members=None):
        self.members=members if members is not None else []
t=goodteam()
s=goodteam()
t.members.append("indu")
print(s.members)
print(t.members)

class EventTicket:
    ticket_counter = 1000
    def __init__(self, attendee_name, event_name, seat_type="General"):
        self.attendee = attendee_name
        self.event = event_name
        self.seat_type = seat_type
        EventTicket.ticket_counter += 1
        self.ticket_id = f"EW-{EventTicket.ticket_counter}"
        self.is_valid = True
    def __str__(self):
        return f"Ticket {self.ticket_id} | {self.attendee} | {self.event} |{self.seat_type}"
t1 = EventTicket("indu", "Tech Fest 2025", "VIP")
t2 = EventTicket("sindhu", "Tech Fest 2025")
print(t1) 
print(t2) 



