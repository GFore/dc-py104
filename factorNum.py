# Given a number, print its factors.

try:
    num = int(input("\nEnter a positive integer: "))

    if num > 0:
        pos = 1
        print ("Factors of %d:" % (num), end=' ')

        while pos <= num/2:
            if num % pos == 0:
                print (pos, end=', ')
            pos += 1
        print(num, "\n")

    else:
        print("you suck at this")


except:
    print("you suck at this")