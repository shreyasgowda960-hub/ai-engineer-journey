#Calculator with functions (Day 3 activity)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def product(a,b):
    return a*b
def division(a,b):
    return a/b
def mod(a,b):
    return a%b

operator=input("Choose operator: + , - , *, / , %:  ")

a=float(input("Enter first no. "))
b=float(input("Enter Second no. "))

if operator=="+":
    print(f"Sum is {(add(a,b))}")

elif operator=="-":
    print(f"Difference is {(subtract(a,b))}")

elif operator=="*":
    print(f"Product is {(product(a,b))}")

elif operator=="/":
    if b==0:
        print("Invalid input")
    else:
        print(f"Division is {(division(a,b))}")

elif operator=="%":
    print(f"Modulus is {(mod(a,b))}")

else:
    print(f"{operator} not defined")

