word="apple"
di={}
for ch in word:
    if ch in di:
        di[ch]+=1
    else:
        di[ch]=1
print(di)


