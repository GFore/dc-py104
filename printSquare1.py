# Print a 5x5 square of * characters.

char = "*"
row = 0
while row < 5:
    col = 0
    while col < 5:
        print(char, end='')
        col += 1
    row += 1
    print()