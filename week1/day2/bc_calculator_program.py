#Bro_Code's calci program Practice

op=input("Enter an Operator: (+ - * / )").strip()

num_1=float(input("Enter first Number: "))
num_2=float(input("Enter second Number: "))

if op == "+":
    result=num_1+num_2
    print(f"{num_1}+{num_2}= {result}")

elif op == "-":
    result=num_1-num_2
    print(f"{num_1}-{num_2}= {result}")

elif op == "*":
    result=num_1*num_2
    print(f"{num_1}*{num_2}= {result}")
elif op == "/":
    if num_2 == 0:
        print("Cannot divide by zero")
    else:
        result=num_1/num_2
        print(f"{num_1}/{num_2}= {result}")
else:
    print(f"{op} is an invalid operator")

