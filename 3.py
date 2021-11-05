from random import randint
number = randint(0,100)

while True:
    guess = int(input("Enter your guess:"))
    if guess < number:
        print("Increase your number.")
    elif guess > number:
        print("Decrease your number.")
    else:
        print("Your guess is TRUE now.")
        break



