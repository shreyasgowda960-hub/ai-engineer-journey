#Collections ate lists, tuples, sets and dictionary




#list

colors = ["green", "blue", "orange", "red"]

print(colors)

#tuple

rgb=(300,22,56)

print("Tuple ",rgb)


#rgb[0]=39

#Dictionaries
student= {"name":"shrey", "grade":"ab", "passed":True}

print(student)
print(student["name"])
print(student["passed"])

#Sets

visited_countries={"america", "india", "india"}
print(visited_countries)
visited_countries.add("israel")
print(visited_countries)


#slicing and indexing
#list
print(colors[0])
print(colors[-1])
print(colors[1:3])

#append remove 
colors.append("megenta")

print(colors)
colors.remove("red")
print(colors)

#dict
student["marks"]=34
print(student)

del student["grade"]
print(student)

#looping in lists and dict

for x in colors:
    print(x)

#best practice

""" 
for color in colors:
    print(color)
"""

for key, value in student.items():
    print(f"{key}: {value}")


