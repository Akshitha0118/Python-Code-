# program for genreating all odd numbers with using forloop where N is +VE
#forloopex4.py
n=int(input("Enter how many odd numbers u want to generate :"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("odd numbers within {}".format(n))
    print("-"*50)
    for i in range(1,n+1,2):
        print("\t{}".format(i))
    else:
        print("-"*50)