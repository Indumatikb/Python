tuple=(1,2,3,4,5)
print(tuple)
print(tuple[2])
print(tuple[-1])
print(len(tuple))
if  9 in tuple:
    print("found")
else:
    print("not found")

t=(1,2,2,3,2,2,7)
value=int(input("enter a number:"))
count=t.count(value)
print("count:",count)
x=t.index(7)
print(x)


t=(1,2,3)
l=list(t)
print(l)

t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1+t2)
