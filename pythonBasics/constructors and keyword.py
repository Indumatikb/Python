class movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def display(self):
        print(f"moviename:{self.title},rating:{self.rating}")

name=movie("kiss",100)
name.display()

class employee:
    def __init__(self,name,designation,salary=3000):
        self.name=name
        self.designation=designation
        self.salary=salary
    
    def display(self):
        print(f"name:{self.name}, designation:{self.designation},salary:{self.salary}")

i=employee("indumati","engii")
k=employee("kavya","dr")
s=employee("shreya","teacher",1500)

i.display()
print()
k.display()
print()
s.display()

    