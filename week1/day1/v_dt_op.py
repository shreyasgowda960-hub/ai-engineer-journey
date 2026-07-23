#var

a=2
b="avb"
c='acb'

print(type(a))
print(type(b))
print(type(c))

c=3
print(c)
print("changed  " + str(type(c)))
print(f"changed {type(c)}")
print("changed", type(c))
f=("changed", type(c))
print(type(f))

# Multiple var

e,  f ,  g=  2.3,   4   , "avb"
print(e,f,g)
print(g,e)

#same val 
a=b=2

#Type Conversions or  TYPE CASTING
# 1. Implicit(auto) 2.Explicit(manual)

#1
z=1
zz=1.2
print(type(z))
print(type(z+zz))

#2

num_str='11'
num_int=5

num_str=int(num_str)
print(type(num_str))
num_int=str(num_int)
print(type(num_int))

#input
name = input("Enter your name: ")   # prompt is optional

print("name is",name, type(name))


#Operators
#Arthemetic
    # + - / // % * **    

o=a+b
p=a**b
q=a//b #floor division

#Assignment

#  = += -= %= *= //= **=

a=f
a +=2 #a=a+2
a **=2 #a=a**2

#Comparision  (returs bolean value)
# == <= >= != < >

#Logical (and or not)




