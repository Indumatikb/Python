class phonebook:
    def __init__(self):
        self.contacts={}

    def add(self, name, number):
        self.contacts[name]=number

    def search(self,name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "not found"
            
obj=phonebook()

obj.add("ravi",9876)
obj.add("asha",9123)

print(obj.search("ravi"))
print(obj.search("jhon"))
