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
flat={}
for usn in students:
    for key in students[usn]:
        new_key = usn + "_"+key
        flat[new_key] = students[usn][key]

print(flat)
