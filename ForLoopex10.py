#program for accepting line of text and count number of words
#forloopex10.py
line=input("enter the line of text :")
words=line.split()
print("given line of text :",line)
for word in words:
    print(word)
print(len(words))