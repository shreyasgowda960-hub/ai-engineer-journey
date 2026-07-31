# with open("doesnotexist.txt", "r") as f:
#     content = f.read()
# print("This line never runs")

try:
    with open("doesnotexist.txt", "r") as f:
       content = f.read()
except FileNotFoundError:
    print("file does not exist")

"""try:
    # code that MIGHT fail
except SomeError:
    # what to do IF that specific error happens"""


#For everything(not good to use)
"""
try:
    with open("data.txt", "r") as f:
        number = int(f.read())
        result = 100 / number
except:
    print("Something went wrong")

"""

# with open("week1/day6/data.txt", "w")as f:
#      f.write("01")


#multiple error handling

try:
    with open("week1/day6/data.txt", "r") as f:
        # input()
        number = int(f.read())
        result = 100 / number
except FileNotFoundError:
    print("The file is missing.")
except ValueError:
    print("The file doesn't contain a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")   



#Finally      
try:
    f = open("week1/day6/data.txt", "r")
except FileNotFoundError:
    print("Not found")
finally:
    print("This always runs, error or not")

    