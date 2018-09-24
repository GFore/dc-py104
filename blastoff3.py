# count down from user value

try:
    n = int(input("Start from: "))

    # allow for cases where n < m and n >= m
    if n < 1:
        print("seriously, dude?")
    else:
        while (n >= 0):
            print(n)
            n -= 1
    print("GO!")
except:
    print("Not a valid number")