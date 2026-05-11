student={
    "usn":"2BL2501"
}

def search(usn):
    if usn in student.values():
        print("found",usn)
    else:
        print("not found")

search("25bjhj")
search("2BL2501")
