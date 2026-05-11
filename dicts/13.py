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

def update_fees(s,new):
    if s in students:
        students[s]["fees"]=new
        print("updated fees")
    else:
        print("not updated")


update_fees("s1",450000)

