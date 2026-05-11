students={
    "2bl25":{
        "name":"indumati",
        "branch":"cse",
        "marks":78,
        "fees":35000
    },

    "2bl24":{
        "name":"nirmala",
        "branch":"ece",
        "marks":90,
        "fees":687999
    },

    "2bl23":{
        "name":"akshatha",
        "branch":"cse",
        "marks":75,
        "fees":780000
    },

    "2bl27":{
        "name":"pavitra",
        "branch":"aiml",
        "marks":99,
        "fees":650000
    }



}


def update_fees(s,new):
    if s in students:
        students[s]["fees"]=new
        print("updated fees")
    else:
        print("not updated")


update_fees("s",450000)

def delete_student(s):
    if s in students:
        del students[s]
        print("deleted")
    else:
        print("not found s")
    

delete_student("s")

def search(usn):
    if usn in students.values():
        print("found",usn)
    else:
        print("not found")

search("25bjhj")
search("2BL2501")