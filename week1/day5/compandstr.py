#Comprehensions and Strings

my_list=[]

for x in range(0,6):
    my_list.append(x*x)

print(my_list)

#can also be written

squares=[x*x for x in range(0,10)]
print(squares)


a=[2]
a=[3]
a=[4]
print(a)

for a in range(1,4):
    print(a)


odd_sq=[x*x for x in range(1,11) if x%2 == 1]    
print(odd_sq)

mult_of_three=[x for x in range(0,20) if x%3==0]
print(mult_of_three)

#Dict

cubes_dict={x: x**3 for x in range(1,6) }
print(cubes_dict)

#string methods
words = ["hi", "there", "friend"]
g="-".join(words)
print(g)

f=" ".join(words)
print(f)

h=".".join(words)
print(h)

#strip and replace

messy="  dog eat dog world     "
l=messy.strip()
print(messy.strip())

p=l.replace("world","earth")

print(p)

#slicing and reversing

s="hello"

print(s[::-1])

print(s[1:4])
print(s[1:4:2])


b="nomenclature"

print(b[2:10:3])

print(b[::-1])

print(b[0:3])