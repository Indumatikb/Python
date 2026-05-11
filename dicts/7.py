def rev_kv(di):
    new={}
    for key, value in di.items():
        new[value]=key
    return new
    

di={"a":1,"b":4}
print(rev_kv(di)) 