# program which will accept a line of text and find the no of words in aline of text  [BY USING WHILE LOOP]
#ForLoopex8.py
s="PYTHON"     # here s is iterable object
print("by using while loop forward direction with +VE")

i=0
while(i<len(s)):
    print("{}".format(s[i]))
    i=i+1

print("by using while loop forward direction with -VE")

i=-len(s)
while(i<=-1):
    print(s[i])
    i=i+1

print(" by using backward direction with +ve")

i=len(s)-1
while(i>=0):
    print(s[i])
    i=i-1


print(" by using backward direction with -VE")

i=-1
while(i>=(-len(s))):
    print(s[i])
    i=i-1