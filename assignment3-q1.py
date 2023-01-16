import random

pc_number = random.randint(0, 20)
n = 0

while True:
    user_number = int(input("Guess the secret number = "))
    n += 1

    if pc_number == user_number:
        print("You won!")
        print("Number of guesses: ", n)
        break

    if pc_number < user_number:
        print("Go lower")

    else:
        print("Go higher")

