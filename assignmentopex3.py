#Progra for accepting any Two Numerical Integer Values and swap them (Interchange)
#AssignmentOpEx3.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("------------------------------------")
print("\tOriginal Value of a={}".format(a))
print("\tOriginal Value of b={}".format(b))
print("------------------------------------")
a=a+b
b=a-b
a=a-b
print("\tSwapped Value of a={}".format(a))
print("\tSwapped Value of b={}".format(b))
print("------------------------------------")