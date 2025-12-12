#KeywordArgex2.py
def disp(a,b,c,d,e=2.71):
    print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,e))
#main program
print("-"*50)
print("\tA\tB\tC\tD\tE")
print("-"*50)
disp(10,20,30,40)
disp(d=40,a=10,b=20,c=30)
disp(e=2.77,d=40,b=20,a=10,c=30)
