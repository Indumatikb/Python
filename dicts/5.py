list = [1,2,2,3,3,3,4]
di={}
for char in list:
    if char in di:
        di[char]+=1
    else:
        di[char]=1
print(di)

