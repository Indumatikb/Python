#1st que
class student:
    def __init__(self,*args,**kwargs):
        self.scores=list(args)
        self.name=kwargs.get("name")
    def display(self):
        return f"{self.name}|{self.scores}"
e=student(23,"indu")
print(e.display())

#2nd que
class config:
    def __init__(self,**kwargs):
        for key, values in kwargs.items():
            setattr(self, key, values)
c=config(name="indu",age=18,branch="CSE")
print(c.name)
print(c.age)
print(c.__dict__)

#2nd que
class database:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            print("database created")
        else:
            print("database not created")
        return cls._instance
    def __init__(self):
        self.connection="connected"
d1=database()
d2=database()
print(d1 is not d2)
print(d1 is d2)

#3rd que
class vectors:
    def __init__(self,x,y=None,z=None):
        if isinstance(x,list):
            self.x=x[0]
            self.y=x[1]
            self.z=x[2]
        else:
            self.x=x
            self.y=y
            self.z=z
    def display(self):
        return (f"{self.x},{self.y},{self.z}")
v=vectors(2,3,4)
b=vectors([5,4,2])
print(v.display())
print(b.display())