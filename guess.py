import random

n = random.randinit(0, 10)
guess = int(input("guess a number between 0 and 10"))

if n == guess:
    print("Topdingiz")
else:
    print("Topa olmadingiz")

