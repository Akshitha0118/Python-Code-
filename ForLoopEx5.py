# program for genreating all odd numbers from N to 1  using forloop where N is +VE
#forloopex5.py
n=int(input("enter how many numbers u want to generate :"))
if(n<=0):
    print("{} is invalid input")
else:
    print("-"*50)
    print("odd numbers from {} to 1 :".format(n))
    print("-"*50)
    if(n%2==0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))