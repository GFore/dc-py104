# program that will prompt you for how many coins you want.
# Initially you have no coins. It will ask you if you want a
# coin? If you type "yes", it will give you one coin, and print
# out the current tally. If you type no, it will stop the program.

ans = "yes"
coins = 0
# print ("You have 0 coins.")

while ans == "yes":
    print ("You have %d coins." % (coins))
    ans = input("Do you want another? ")
    if ans == "yes":
        coins += 1

print("Bye")