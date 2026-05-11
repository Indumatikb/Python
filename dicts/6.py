words=["apple","ant","banana","ball"]
di={}
for word in words:
    first=word[0]
    print(first)
    if first in di:
        di[first].append(word)
    else:
        di[first]=[word]

print(di)



words=["shreya","sindhu","akshata","aouri"]
di={}
for word in words:
    first=word[0]
    if first in di:
        di[first].append(word)
    else:
        di[first]=[word]

print(di)