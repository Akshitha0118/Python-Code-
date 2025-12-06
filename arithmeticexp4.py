#ArithmeticOpEx4.py
wamt=int(input("Ennter How Much Amount u want to withdraw:"))
notes500=wamt//500
wamt=wamt%500
notes200=wamt//200
wamt=wamt%200
notes100=wamt//100
wamt=wamt%100
print("\t\tNumber of 500={}".format(notes500))
print("\t\tNumber of 200={}".format(notes200))
print("\t\tNumber of 100={}".format(notes100))