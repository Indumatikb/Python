#1st question
class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def drive(self):
        print(f"{self.brand}is driving the vehicle with {self.speed}")
c=car("maruti suzuki",129.9)
print(c.drive())

#second question
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c=circle(2)
print(c.area())

#third question
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return self.name
    
a=person("indumati",18)
b=person("poojaa",19)
c=person("sindhuu",16)

print(a.display())
print(b.display())
print(c.display())
