import random

no = random.randint(0,9)
attempts = 0

while True:
    try:
        y = int(input("Guess the no.: "))
    except ValueError:
        print("Don't enter text")
        continue

    attempts += 1

    if y == no:
        print(f"Right on, {no} was the number! It took you {attempts} tries.")
        break
    elif y < no:
        print("you guessed lower, try again")
    else:
        print("you guessed higher, try again")
