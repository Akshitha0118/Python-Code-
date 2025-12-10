# program to generate mul table by using while and for loop
#ForLoopex7.py
n=int(input("enter the mul table:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-" * 50)
    print("mul table using while loop ")
    print("-" * 50)
    i=1
    while(i<=10):
        print("{} x {}= {}".format(n,i,n*i))
        i=i+1
    else:
        print("-"*50)
        print("mul table using for loop ")
        print("-" * 50)
        for i in range(1,11):
            print("{} x {}= {}".format(n,i,n*i))
        else:
            print("-" * 50)