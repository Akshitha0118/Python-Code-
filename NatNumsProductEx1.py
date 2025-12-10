#program for Finding Product of 'N' Natural Nums
#NatNumsProductEx1.py
n=int(input("enter how many natural num product u want:"))
if(n<=0):
    print("\t{}".format(n))
else:
    p=1 # multiplicative identity
    for i in range(1,n+1):
        print(i)
        p=p*i
    else:
        print("product={}".format(p))