#program for generating all even nunbers with for loop where N is +VE
n=int(input("Enter how many numbers u want to generate:"))
if(n<=0):
    print("{} is invalid number".format(n))
else:
    print("-"*50)
    print("Even numbers with in range {}".format(n))
    print("-"*50)
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
        print("-"*50)