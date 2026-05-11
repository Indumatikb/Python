#1 que
foods=["idli","dosa","rotti","puri"]
nefoods=[food.upper()for food in foods]
print(nefoods)

#sec que
items={
    "rice":55,
    "milk":30,
    "curd":15,
    "ice":100,
    "cake":300

}
total=0
for item in items:
    total=total+items[item]
print(total)

#3 que
l=[i for i  in range(1, 11)]
print(l)
dl=[i**2 for i in l]
print(dl)

#4 que
lists={
    "list1":{
        "name":"indu",
        "age":18,
        "marks":24
    },
    "list2":{
         "name":"shreya",
        "age":18,
        "marks":25
    },
    "list3":{
         "name":"shreysh",
        "age":18,
        "marks":25
    }

}

for list in lists.values():
    print("name:", list["name"])
    print("age:", list["age"])
    print("marks:", list["marks"])
    print()

#5 que
cities ={
    "banglore":130000000,
    "mysore":3000000,
    "hubballi":40000

}
filtered_citeies={city:pop for city, pop in cities.items()if pop < 1000000}
print(filtered_citeies)

#6 que
matrix=[
    [1, 3, 4],
    [5, 6, 7],
    [8, 9, 5]
]
for ro in matrix:
    print(ro)
for ro in matrix:
    print("sum of ro:",sum(ro))