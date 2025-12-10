#Program for Generating N TO 1 numbers where N is +ve
#WhileLoopEx2.py
n=int(input("enter the number of values u want to generate :"))
if(n<=0):
    print("it is an invalid number")
else:
    print("-" * 40)
    i=n
    while(i>=1):
        print("{}".format(i))
        i=i-1
    else:
        print("-"*40)