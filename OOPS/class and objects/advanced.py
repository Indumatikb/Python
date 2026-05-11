#1st question
class matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] 
                   for j in range(len(self.matrix))] 
                   for i in range(len(self.matrix))]
        return matrix(result)
m1=matrix([[1,2],[2,3]])
m2=matrix([[1,2],[2,3]])
m3=m1+m2
print(m3.matrix)

#second question
class student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
class classroom:
    def __init__(self):
        self.student_list=[]
    def add_student(self,student):
        self.student_list.append(student)
    def topper(self):
        tpr = max(self.student_list, key=lambda s: sum(s.scores))
        return (f"topper of the class is {tpr.name}",tpr)
    def average(self):
        all_scores = [score for s in self.student_list for score in s.scores]
        avg=sum(all_scores)/len(all_scores)
        return avg

s1=student("indu",[90,30,40])
s2=student("sindhu",[34,45,85])
s3=student("nisha",[43,76,89])

c=classroom()
c.add_student(s1)
c.add_student(s2)
c.add_student(s3)

print(c.topper())
print(c.average())

#4th que
class event:
    def __init__(self,event_name,capacity):
        self.event_name=event_name
        self.capacity=capacity
        self.registred=[]
        self.waitlist=[]
    def register(self,name):
        if len(self.registred)<self.capacity:
            self.registred.append(name)
            print("registred successfully for the event")
        else:
            self.waitlist.append(name)
            return "wait for sometime"
    def show_event(self):
        print(f"event name :{self.event_name}")
        print(f"regeistred: {self.registred}")
        print(f"watinglist: {self.waitlist}")
class attendance:                   
    def __init__(self, event):      
        self.event = event
        self.attended = []
    def mark(self,name):
        if name in self.event.registred:
            self.attended.append(name)
            print( f"{name} attended the event")
        else:
            print(f"{name} not attended the event")
    def show_attendence(self):
        print(f'attended:{self.attended}')

e=event("python workshop",capacity=30)
e.register("liya")
e.register("maya")
e.register("zoya")
e.show_event()

a=attendance(e)
a.mark("liya")
a.mark("loya")
a.mark("nirm")
a.show_attendence()
