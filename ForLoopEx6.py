# program for genreating all even numbers from N to 1  using forloop where N is +VE
#forloopex7.py
n=int(input("Enter how many even numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("even numbers within {} :".format(n))
    print("-"*50)
    if(n%2!=0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("-"*50)