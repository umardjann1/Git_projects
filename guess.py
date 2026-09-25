import random

n = random.randint(0, 10)


while True:
    guess = int(input("Guess a number between 0 and 10: "))
    if n == guess:
        print("Topdingiz!")
        break
    else:
        print("Noto'g'ri, qaytadan urinib ko'ring")


