# python program tp generate odd numbers in reverse order within range of N
n=int(input("enter how many odd numbers u want to generate in reverse order : "))
if(n<=0):
    print("invalid number")
else:
    print("-"*50)
    if(n%2==0):
        n=n-1
    i=n
    while(i>=1):
        print("\t{}".format(i))
        i=i-2





