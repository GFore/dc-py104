# Print the multiplication table for numbers from 1 up to 10. 

num = 1

while num <= 10:
    multby = 1
    while multby <= 10:
        print(num, "X",  multby, "=", num * multby)
        multby += 1
    num += 1
    print()