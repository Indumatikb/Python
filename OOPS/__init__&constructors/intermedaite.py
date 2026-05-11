#1 question
class student:
    def __init__(self,name):
        self.name=name
        self.scores=[]
    def add_scores(self,scores):
        self.scores.append(scores)
    def display(self):
        avg=sum(self.scores)/len(self.scores)
        return avg
s=student("sindhuu")
s.add_scores(90)
s.add_scores(89)
s.add_scores(90)
print(s.display())

#2que
class student:
    def __init__(self,name,scores=None):
        self.name=name
        self.scores=scores if scores is not None else []
    def average(self):
        avg=sum(self.scores)/len(self.scores)
        return avg
s=student("indu",[10,10])
print(s.average())

#3rd ques
class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def add_validity(self):
        if self.price>0 and self.stock>=0:
            return "they have their validate product and stock"
        else:
            return "invalid bro!"
p=product("waterbottle",300,3)
q=product("waterbottle",30,-1)
print(p.add_validity())
print(q.add_validity())

class eventwaala:
    counter=0
    def __init__(self,name,event_name):
        eventwaala.counter+=1
        self.organizer_id=f"EW00 {eventwaala.counter}"
        self.name=name
        self.event_name=event_name
    def display(self):
        return (f"{self.organizer_id} | {self.name} | {self.event_name} ")

e=eventwaala("indu","tech-fest")
e1=eventwaala("sindhu","rangmanch")
print(e1.display())
print(e.display())

    
