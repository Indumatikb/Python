students={
    "2bl25":{
        "name":"indumati",
        "fees":905000,
        "branch":"cse"
    },

    "2bl24":{
        "name":"nirmala",
        "fees":60080,
        "branch":"ece"
    }
}

max_fee=0
for usn in students:
    fees=students[usn]["fees"]
    if fees>max_fee:
        max_fee=fees
print(f" high fees",max_fee)