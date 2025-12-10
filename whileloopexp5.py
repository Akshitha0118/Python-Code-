#Program for Generating all even   numbers where N is +ve
#WhileLoopEx5.py
n=int(input("enter how many even numbers u want to generate:"))
if(n<=0):
    print(" it is an invalid number")
else:
    print("-"*40)
    i=1
    while(i<=n):
        if(i%2==0):
            print("{}".format(i))
        i=i+1
    else:
        print("-"*40)
