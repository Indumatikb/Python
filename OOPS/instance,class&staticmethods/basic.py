class temperature:
    unit="celcius"
    def __init__(self,value):
        self.value=value
    def display(self):
        return (self.value*9/5)+32

    @classmethod
    def set_unit(cls,unit):
        cls.unit=unit
    @classmethod
    def from_farenheit(cls, f_value):
        return cls((f_value-32)*5/9)


    @staticmethod
    def is_valid(value):
        return -273.15 <= value <= 1

t=temperature(273)
print(t.display())
t1=temperature.from_farenheit(100)
print(t1.value)
print(temperature.is_valid(t1.value))


#1st ques
class circle:
    def __init__(self,radius):
        self.radius=radius
    def display(self):
        return 3.14*self.radius*self.radius
    
    @classmethod
    def unit(cls, unit):
        cls.unit_name=unit
    
    @staticmethod
    def is_positive(value):
        return value>0
    
c=circle(2)
print(c.display())
c1=circle.unit("cm")
print(circle.unit_name)
print(circle.is_positive(5))

#2nd que
class circle:
    def __init__(self,radius):
        self.radius=radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
c=circle.from_diameter(20)
print("circle is created by",c.radius,"radius")

#3rd que
class math_helper:
    @staticmethod
    def add(n1,n2):
        sum=n1+n2
        return sum
    @staticmethod
    def substract(n1,n2):
        sub=n1-n2
        return sub
    @staticmethod
    def multiply(n1,n2):
        mul=n1*n2
        return mul
    @staticmethod
    def divide(n1,n2):
        div=n1/n2
        return div
    
print(math_helper.add(1,2))
print(math_helper.substract(3,2))
print(math_helper.multiply(5,10))
print(math_helper.divide(10,2))

