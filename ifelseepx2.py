#program for accepting a value and decide whether It is +VE or -VE or Zero
#IfElseStmtEx2.py
value=float(input("Enter Any Numerical Value:")) # 10
if(value>0):
    print("\t{} is +VE Value".format(value))
else:
    if(value<0):
        print("\t{} is -VE Value".format(value))
    else:
        print("\t{} is ZERO".format(value))
    print("Other part of Inner if..else Stmts")
print("Other part of Outer if..else Stmts")