#Progra for accepting any Two Values and swap them (Interchange)
#AssignmentOpEx2.py
a,b=input("Enter Value of a:"),input("Enter Value of b:")
print("------------------------------------")
print("\tOriginal Value of a={}".format(a))
print("\tOriginal Value of b={}".format(b))
print("------------------------------------")
t=a  # Single Line assignment
a=b
b=t
print("\tSwapped Value of a={}".format(a))
print("\tSwapped Value of b={}".format(b))
print("------------------------------------")