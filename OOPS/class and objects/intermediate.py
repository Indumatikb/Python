#first question
class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            return "amount added successfully"
        else:
            return "your amount cannot be enetered"
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            return "amount withdrawl succesful"
        else:
            return "sry! you cannot take amount now"
        
b=bank(1000)
b.deposit(500)
b.withdraw(500)
print(b.balance)

#second question
class bank:
    def __init__(self,balance,intrest_rate):
        self.balance=balance
        self.intrest_rate=intrest_rate
    def apply_intrest(self):
        return self.balance+self.balance*self.intrest_rate/100
b=bank(1000,10)
print(b.apply_intrest())

#third question
class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        return "book added successfully"
    def remove_book(self,book):
        self.books.remove(book)
        return "book removed successfully"
    def list_books(self):
        return self.books
    
l=library()
l.add_book("mahabharat")
l.add_book("wings of fire")
l.add_book("laughter")
l.add_book("jo")
l.remove_book("wings of fire")
print(l.list_books())

class event:
    def __init__(self):
        self.items={}
    def add_item(self,items,quantity):
        if items in self.items:
            self.items[items]+=quantity
        else:
            self.items[items]=quantity
    def remove_items(self,items,quantity):
        if items in self.items:
            self.items[items]-=quantity
        else:
            self.items[items]=quantity
    def check_items(self):
        return self.items
e=event()
e.add_item("mice",2)
e.add_item("chairs",30)
e.remove_items("mice",2)
print(e.check_items())

