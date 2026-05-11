students={
    "s1":{
        "name":"indumati",
        "fees":25000,
        "usn":"2bl25"
    },

    "s2":{
        "name":"nirmala",
        "fees":60080,
        "usn":"2bl26"
    }
}

def delete_student(s):
    if s in students:
        del students[s]
        print("deleted")
    else:
        print("not found s")
    

delete_student("s")