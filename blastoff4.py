# count down from user value confirmed to be no larger than 20

try:
    while True:
        n = int(input("Start from: "))
        if n>20:
            print("Too high")
        else:
            break

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