#1que(a)
my_tuple=("suzuki", "honda", "benz", "kea", "lamborginni")
#tuple doesn't modify they are fixed 

#b
t=(10, 30, 50, 70)
print(t[1:3])

#c
t1=[1,4,6,7]
t11=[3,5,7,9]
t111=t1+t11
print(t111)

#sec que 
my_fav={"custardapple", "apple", "guava"}
frnd_fav={"banana", "orange", "apple"}
print(my_fav|frnd_fav)
print(my_fav&frnd_fav)
my_fav.add("mango")
print(my_fav)
my_fav.remove("apple")
print(my_fav)
my_fav.discard("custardapple")
print(my_fav)
my_fav.remove("carrot") #'ll get error at this position
print(my_fav)



#3rd que
list=[1,4,6,9]
t=tuple(list)
print(t)



f=set(list)
print(f)
f.add(7)
print(f)
t.add(7)
print(t)
