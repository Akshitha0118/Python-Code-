#Program for generating N to 1 by using for loop  where N is +VE
#ForLoopEx2.py
n=int(input("enter how many numbers u want to generate:"))
if(n<=0):
    print("{} is invalid number".format(n))
else:
    print("-" * 50)
    print("numbers from {} to 1 ".format(n))
    print("-" * 50)
    for i in range(n,0,-1):
        print("\t{}".format(i))
    else:
        print("-"*50)