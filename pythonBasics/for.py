'''
for i in range(1,31):
    print(i*3)
    

for i in range(1, 11):
    print(i+1)


name=input("enter your name:")
for letter in name:
    print(letter)
    

string=input("enter any string:")
vowels="a, e, i, o, u"
for char in string:
    if char in vowels:
        print(vowels)

        '''
sec = int(input("enter the seconds: "))
hours = sec // 3600
sec = sec%3600
minutes= sec//60
sec = sec%60
print("hours", hours)
print("minutes", minutes)
print("seconds", sec)