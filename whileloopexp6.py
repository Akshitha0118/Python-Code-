#python program to generate odd numbers from range of N where N is +ve
n=int(input("enter how many odd numbers u want to generate :"))
if(n<=0):
    print("invalid number")
else:
    i=1
    while(i<=n):
        print("{}".format(i))
        i=i+2
    else:
        print("-"*50)