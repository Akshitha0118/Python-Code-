# program which will accept a line of text and find the no of words in aline of text  [BY USING FOR LOOP]
#ForLoopex9.py
s="Hyderabad"  # here s is iterable object

for ch in s:
    print(ch)
print("-"*55)
for ch in s[::-1]:
    print(ch)

print("forward direction with +ve")
for i in range(0,len(s)):
    print(s[i])
print("forward direction with -ve")
for i in range(-len(s),0):
    print(s[i])
print("backward direction with +ve")
for i in range(len(s)-1,-1,-1):
    print(s[i])

print("backward direction with +ve")
for i in range(-1,-(len(s)+1),-1):
    print(s[i])