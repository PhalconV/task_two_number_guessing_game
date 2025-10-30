
# import necessary libraries
import random




# Number Guessing Game Mini Project
# Initialize random
digit = random.randint(1, 10)
trial = None


# Whi
while trial != digit:
    trial = input("Enter a number between 1 and 10: ")
    trial = int(trial)

    if trial > digit:
        print("Your guess is too high. Try Again \u267B")
    elif trial == digit:
        print("You have guessed right \U0001F44F")
    else:
        print("You have guess too low. Try Again \u274c")
