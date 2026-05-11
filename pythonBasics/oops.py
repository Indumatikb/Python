class vehicle:
    def start(self):
        print("vehicle is started")

class bike(vehicle):
    def ride(self):
        print("bike is being ridden")


b=bike()
b.start()
b.ride()


class shapes:
    def calculate_area(self):
        return 0
class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius*self.radius
    
class rectangle(shapes):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        return self.length*self.breadth
    
shapes=[circle(4),rectangle(13,10)]

for shape in shapes:
    print("area: ",shape.calculate_area())