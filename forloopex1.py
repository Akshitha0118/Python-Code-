#program for generating 1 to N by using for loop where N is +VE
n=int(input("enter how many numbers u want to generate :"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers within :{}".format(n))
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-"*50)