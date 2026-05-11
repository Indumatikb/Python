students={
    "2bl25":{
        "name":"indumati",
        "fees":25000,
        "branch":"cse"
    },

    "2bl24":{
        "name":"nirmala",
        "fees":60080,
        "branch":"ece"
    }
}


def branch_totalfees():
    result={}
    for usn in students:
        branch=students[usn]["branch"]
        fees=students[usn]["fees"]

        if branch in result:
            result[branch]+=fees
        else:
            result[branch]=fees

    print(result)

branch_totalfees()