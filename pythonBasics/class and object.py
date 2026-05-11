
class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def display(self):
        print("brand:", self.brand)
        print("price:", self.price)

m1= mobile("samsang",1500000)
m11=mobile("vivo", 13000)
    

m1.display()
print()
m11.display()



class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks=marks
    def display(self):
        print("name",self.name)
        print("marks", self.marks)

s1 = student("indu",45)
s11 = student("aksh", 48)
s111 = student("shreya", 50)

s1.display()
print()
s11.display()
print()
s111.display()
        
    