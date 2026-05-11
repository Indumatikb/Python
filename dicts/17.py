students={
    "2bl25":{
        "name":"indumati",
        "branch":"cse"
    },

    "2bl24":{
        "name":"nirmala",
        "branch":"ece"
    },

    "2bl23":{
        "name":"akshatha",
        "branch":"cse"
    },

    "2bl27":{
        "name":"pavitra",
        "branch":"aiml"
    }



}

di={}
for usn in students:
    branch=students[usn]["branch"]
    if branch in di:
        di[branch]+=1
    else:
        di[branch]=1

print(di)

