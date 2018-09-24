# Print a NxN square of * characters. Prompt the user for N.

char = "*"
row = 0

try:
    N = int(input("How big is the square? "))
    while row < N:
        col = 0
        while col < N:
            print(char, end='')
            col += 1
        row += 1
        print()

except:
    print("Not a valid integer")