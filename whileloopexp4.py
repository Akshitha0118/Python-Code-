#Program for Generating all even   numbers where N is +ve
#WhileLoopEx4.py
n=int(input("enter how many even numbers u want to generate:"))
if(n<=0):
    print("it is an ivalid number ")
else:
    print("-"*40)
    i=2
    while(i<=n):
        print("{}".format(i))
        i=i+2
    else:
        print("-"*40)
    print("execution completed")