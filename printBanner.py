# Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************

char = "*"
row = 1

try:
    msg = input("Text? ")
    width = len(msg) + 4
    fullrow = char * width
 
    print(fullrow)
    print(char + " " + msg + " " + char)
    print(fullrow)

except:
    print("Not a valid integer")