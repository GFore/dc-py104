# Number guessing game
import random
playing = "Y"

#while True:
while playing == "Y":
    secret_number = random.randint(1, 10)

    num_guesses = 5
    print("\nI am thinking of a number between 1 and 10.")
    print("You have %d guesses left." % (num_guesses))

    while num_guesses > 0:
        try:
            guess = int(input("What's the number? "))
        except:
            print("Try again")
            continue
        if guess == secret_number:
            print("Yes! You win!")
            break
        elif guess < 1 or guess > 10:
            print("I don't think you are paying attention")
        elif guess < secret_number:
            print("%d is too low." % (guess))
        else:
            print("%d is too hi." % (guess))
        
        num_guesses -= 1
        if num_guesses == 0:
            print("You ran out of guesses!")
            break
        else:
            print("You have %d guesses left." % (num_guesses))

    print()
    playing = input("Do you want to play again (Y or N)? ")

print("Bye\n")