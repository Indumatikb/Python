#1que
'''
cities={
    "bijapur":"rotti",
    "davangere" :"bennedose",
    "belgavi":"kunda",
    "mandya":"kabbu",
    "mysore":"mysorepak"  
    }
cities["banglore"]="bisibelebaath"
print(cities) 
cities["banglore"]="panipuri"
print(cities)
cities.pop("bijapur")
print(cities)

print("city name:")
print(cities.keys())

print("dish names:")
print(cities.values())

#sec que
friends={
    "friend1":{
        "name":"indu",
        "fav_subject":"chemistry",
        "fav_food":"pizza"
    },
    "friend11":{
        "name":"spoorti",
        "fav_subject":"biology",
        "fav_food":"pizza"
    }
}

print("fav_food of indu:",
friends["friend1"]["fav_food"])
'''

student={
    "USN1":{
        "name":"indumati",
        "branch":"CSE",
        "fee":50000,
        "marks":50.85
    }
}

print(student)

student["USN2"]="name:akash","branch:CSE","fee:121000","marks:77.7"
student["USN3"]="name:amit","branch:ece","fee:134000","marks:65.3"
student["USN4"]="name:akarsh","branch:ise","fee:421000","marks:43.78"
student["USN5"]="name:aditi","branch:aiml","fee:234433","marks:90.6"
print(student)

def update_fee(s,new):
    if s in student:
        student[s]["fee"]=new
        print("updated fees")
    else:
        print("not updated")

update_fee("USN1",121000)
print(student)

def delete_student(s):
    if s in student:
        del student[s]
        print("deleted")
    else:
        print("not deleted")

delete_student("USN2")
print(student)

di={}

for usn in student:
    branch=student[usn]["branch"]
    if branch in di:
        di[branch]+=1
    else:
        di[branch]=1

print(di)

max_marks=0
for usn in student:
    marks=student[usn]["marks"]
    if marks>max_marks:
        max_marks=marks
        print("high scored",marks)
    else:
        print("low score but its okay")
