#DefaultArgsex3.py
def dispstudvals(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))
#main program
print("-"*50)
print("\tsno\tname\tmarks\tcourse\tcountry")
print("-"*50)
dispstudvals(300,"DR",56.88)
dispstudvals(400,"SS",67.00,"JAVA")
dispstudvals(600,"Dt",15.15,cnt="usa")
