import random

n = random.randint(0, 10)
guess = int(input("Guess a number between 0 and 10: "))

guesses = 0

while True:
    if n == guess:
        print("Topdingiz!")
        break
    if guesses >= 3:
        print("Yutqazdingiz ")
        break


