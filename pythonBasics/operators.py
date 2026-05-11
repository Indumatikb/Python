
#1st que
first=int(input("enter first number: "))
second=int(input("enter second number: "))
print(first>0 and second>10)
print(first>10 or second>10)
print(not(first>10))

#sec que
age=int(input("enter your age:"))
if age>=18:
    print("you are an adult")
else:
    print("you are minor")


#3rd que
string=input("enter any string value: ")
print('a' in string)
print('python'not in string)


#4th que
a=int(input("enter the num: "))
b=int(input("enter the num: "))

print("a&b", a&b)
print("a^b",a^b)
print("a|b",a|b)
print("a<<2",a<<2)
print("a>>1",a>>1)