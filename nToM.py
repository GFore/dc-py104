# prompt the user for the number to start on (n) and the number to end on (m)
# and then print out the numbers from n to m inclusive

try:
    n = int(input("Start from: "))
    m = int(input("End on: "))

    # allow for cases where n < m and n >= m
    if n < m:
        while (n <= m):
            print(n)
            n += 1
    else:
        while (n >= m):
            print(n)
            n -= 1

except:
    print("Not a valid number")