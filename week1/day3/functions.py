def say_hi():
    print("Hi there!")

say_hi()


say_hi()

def greet(name):
    print(f"hello {name}")

greet("shrey")    

def add(a,b):
    total=a+b
    print(f"sum is: {total}")

add(3,5)

#with return

def addr(a,b):
    return a+b

resultant_addition=addr(5,6)
print(resultant_addition*5)
print(f"it is {resultant_addition*2}")

#Default
name="avi"
def hello(name="Shrey"):
    print(f"hello {name}")

hello()
hello("avin")

def power(base,exponent=2):
    return pow(base,exponent)

power_1=power(2)
power_2=power(2,4)

print(f"Default: {power_1}")
print(f"Default'nt: {power_2}")

#Multiple Parameters

def stats(a,b):
    return a+b, a*b

print(stats(2,3))

total, product= stats(20,2)

print(total)
print(product)

#Global and Local Variables

def describe(name, age):
    print(f"{name} is {age} years old")

describe("Appu", 10)

name="Abi"
age=16
def describe_v2():
    print(name)
    print(age)
describe_v2()    