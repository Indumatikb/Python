students={
    "2bl25":{
        "name":"indumati",
        "branch":"cse",
        "marks":9.1
    },

    "2bl24":{
        "name":"nirmala",
        "branch":"ece",
        "marks":8
    },

    "2bl23":{
        "name":"akshatha",
        "branch":"cse",
        "marks":9
    },

    "2bl27":{
        "name":"pavitra",
        "branch":"aiml",
        "marks":9.6
    }



}
max_marks=0
for usn in students:
    marks=students[usn]["marks"]
    if marks>max_marks:
        max_marks=marks

print("topper is {usn}",max_marks)
