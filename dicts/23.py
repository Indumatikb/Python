class anagrams:
    def group (self,words):
        di={}

        for word in words:
            key="".join(sorted(word))

            if key in di:
                di[key].append(word)
            else:
                di[key]=[word]
        return list(di.values())

obj=anagrams()
print(obj.group(["eat","tea","tan","ate"]))            