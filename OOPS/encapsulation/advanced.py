class datastore:
    def __init__(self):
        self.__storage={}
    def set_value(self,key,value):
        self.__storage[key]=value
    def get_value(self,key):
        return self.__storage.get(key)
    def delete_value(self,key):
        self.__storage.pop(key)
        return "deleted"
 
d=datastore()
d.set_value("name","indumati")
d.set_value("age",18)
print(d.get_value("name"))
print(d.get_value("age"))
print(d.delete_value("name"))

class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError("cannot modify immutable points")
        super().__setattr__(name,value)
    def display(self):
        return (self.x,self.y)
p=points(3,4)
p.x=10
print(p.display())






