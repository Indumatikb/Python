class worddi:
    def count(self,text):
        words=text.split()
        di={}
        for word in words:
            if word in di:
                di[word]+=1
            else:
                di[word]=1
        return di

obj=worddi()
print(obj.count("the cat and the dog and the cat"))