d1={"a":1,"b":2}
d2={"c":3,"d":4}
d1.update(d2)
print(d1)

def merg_di(d1,d2):
    d1.update(d2)
    return d1
d1={"a":1,"b":2}
d2={"c":3,"d":4}

result=merg_di(d1,d2)
print(result)
