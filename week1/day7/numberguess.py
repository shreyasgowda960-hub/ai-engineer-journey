import random
try:
    no=random.randint(0,9)
    y=int(input("Guess the no."))
    while y!=no:
        if y<no:
            print("you guessed lower,try agian")
        elif y>no:
            print("you guessed higher.try again")    
        y=int(input("Guess again: "))    

    print(f"Right on, {no} was the number")
except ValueError:
    print("Don't enter text")
