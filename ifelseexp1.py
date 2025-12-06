#program for accepting a value and decide whether It is Palindrome or Not
#IfElseStmtEx1.py
value=input("Enter Any Value:") # RADAR
if(value.lower()==value[::-1].lower()):
    print("\t{} is Plaindrome".format(value))
else:
    print("\t{} is Not Plaindrome".format(value))
print("Program Execution Completed")