'''student_information={
    "name":"indumati",
    "USN":"2BL25CS042",
    "branch":"comouter science and engineering"
}

print(student_information)'''

keys = ["name","usn","branch"]
values = ["Akash","2BL25CS001","CSE"]
di ={}

for i in range(len(keys)):
    print(i)
    di[keys[i]]=[values[i]]
print(di)