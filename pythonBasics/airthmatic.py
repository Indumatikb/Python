'''#1 question
a = 9 
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# sec question
x = 9
y = 8
x, y = y, x
print("x= ", x)
print("y= ", y)
sum=0
for i in range(1,11):
    if i%2==0:
        sum=sum+i
print(sum)

sum=0
num=(input("enter the number:"))
x=num[::-1]
print(x)
num=int(num)
print(num)
a=type(num)
print(a)
sum=sum+num
print(num)
'''

n=5873
num=n
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10





