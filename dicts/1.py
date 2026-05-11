string = input("enter the string: ")
print(string)
di={}
for ch in string:
    if ch in di:
        di[ch]+=1
    else:
        di[ch]=1
print(di)




    
