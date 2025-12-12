#possArgex1,py
def dispstudvals(sno,sname,marks):
    print("\t{}\t{}\t{}".format(sno,sname,marks))
#main program
print("-"*50)
print("\tSno\tName\tMarks")
print("-"*50)
dispstudvals(100,"RS",45.67)
dispstudvals(200,"TR",65.17)
dispstudvals(300,"DR",77)
dispstudvals(400,"SS",34)
dispstudvals(500,"SS",78)
dispstudvals(marks=90,sname="TT",sno=600)