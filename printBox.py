# Given a height and width, input by the user, print a box consisting of * characters as its border.

char = "*"
row = 1

try:
    # get box size from user
    width = int(input("Width? "))
    height = int(input("Height? "))

    fullrow = char * width
    midrow = (width-2) * " "

    print(fullrow)                  # print top row
    while row < height-1:
        row += 1
        print(char + midrow + char)
    print(fullrow)                  # print bottom row

except:
    print("Not a valid integer")