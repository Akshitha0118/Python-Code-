#program for demonstrating the concept of default arguments -- used for specifying common data
#DefaultArgsex1.py
def disptudvals(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
#main program
print("-"*50)
print("\tSNO\tName\tMarks\tCourse")
print("-"*50)
disptudvals(100,"RS",45.67)
disptudvals(200,"TR",67.44)
disptudvals(300,"DR",25.14)
disptudvals(400,"SS",75.14)
disptudvals(400,"SS",75.14)