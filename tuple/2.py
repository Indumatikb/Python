t=(1,2,3,4,5,6,7,8,9,10)
print(max(t))
print(min(t))
print(sum(t))
en= tuple(i for i in range (1,11) if i%2==0)
print(en)
print(en[::-1])
print(en[:3])
print(enumerate(en))

tu=((1,2),(3,4))
print(tu)
    
t1=(1,2,3)
t2=(4,5,6)
nestde_tuple=(t1,t2)
print(nestde_tuple)

g=(1,2,2,3,1)
freq={}
for ch in g:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

t = (1, 2, 2, 3, 1)

freq = {}

for x in t:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)

a=(10,20,30,20,40)
a=tuple(set(a))
lst=list(a)
lst.sort()
print("second largest:",lst[-2])

t = (10, 20, 30, 20, 40)

t = tuple(set(t))   # remove duplicates
lst = list(t)
lst.sort()

print("Second largest =", lst[-2])

t1=(100,200,300,800,400)
t2=(500,600,700,800,200)
x=(t1+t2)
x=tuple(set(x))
print(x)

t=('c','a','a','c')
if t==t[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

t1=(2,3,5,6)
t3=(4,6,8,9)
common=tuple(set(t1)&set(t3))
print(common)

n=10
lst=[]
for i in range(1,n+1):
    lst.append(i*i)
t=tuple(lst)
print(t)

t=(1,2,3)
l=list(t)
print(l)