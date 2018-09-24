# Print the first 100 triangle numbers. 

num = 1
try:
    goto = int(input("How many? "))
except:
    print("Bad entry, I will choose for you... 100:")
    goto = 100

while num <= goto:
    tot = 0
    trinum = num
    while trinum > 0:
        tot += trinum
        trinum -= 1
    
    print(num, ":", tot, " | ", end=' ')
    num += 1

    if num % 5 == 0: print()
print()