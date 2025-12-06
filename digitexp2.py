##program for accepting any Digit and display its name
#DigitEx2.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter Ur Digit:")) # 0 1 2 3 4 5 6 7 8 9
print("{} is {}".format(dig,d.get(dig) if d.get(dig)!=None else "NUMBER" if (dig > 9) else "-VE DIGIT" if dig in [-1, -2, -3, -4, -5, -6, -7, -8, -9] else "-VE NUMBER"))