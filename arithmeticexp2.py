#program for Cal simple Interest and total amount to pay
#ArithmeticOpEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter rate of interest:"))
#Cal si and totamt
si=(p*t*r)/100
totamt=p+si
print("*"*50)
print("\tSimple Interest Result")
print("*"*50)
print("\t\tPrinciple Amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of Interest:{}".format(r))
print("\t\tSimple Interest:{}".format(si))
print("\t\tTotal Amount to pay:{}".format(totamt))
print("*"*50)