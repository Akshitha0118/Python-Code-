#Program for Generating 1 to N numbers where N is +ve
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:")) # 10
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-" * 50)
    i=1 # Initlization Part
    while(i<=n): # Conditional Part
        print("\t{}".format(i))
        i=i+1 # Updation part
    else:
        print("-"*50)
    print("Other Statements in Program")
