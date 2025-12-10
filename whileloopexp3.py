#Program for Generating N to 1 numbers where N is +ve
#WhileLoopEx3.py
n=int(input("enter a values u want to generate :"))
if(n<=0):
    print("it is an invalid number ")

else:
    print("-"*40)
    while(n>=1):
        print("{}".format(n))
        n=n-1
    else:
        print("-"*40)