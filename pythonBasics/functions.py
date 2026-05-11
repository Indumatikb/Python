multiply=lambda a, b: a*b
print(multiply(3, 4))

#2 que
def add_num(n):
    if n==0:
        return 0
    else:
        return n + add_num(n-1)
    
print(add_num(5))

#3 que
def average(*numbers):
    return average(numbers)
print(average(10,10))