class Dog:
    def __init__(self, name):
        self.name = name

    def whoami(self):
        print(f"self is: {self}")
        print(f"my name is: {self.name}")

a = Dog("Rex")
b = Dog("Bella")
a.whoami()
b.whoami()


print()
print()
print()
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, times=1):
        for _ in range(times):
            print(f"{self.name}: woof!")

    def human_age(self):
        return self.age * 7        # returns, doesn't print


d = Dog("Rex", 3)
d.bark(3)
print(d.human_age())



print()
print()
print()

class Dog:
    species = "Canis familiaris"      # class attribute — shared

    def __init__(self, name):
        self.name = name              # instance attribute — per object


a = Dog("Rex")
b = Dog("Bella")
print(a.species, b.species)    # both print the same thing
print(a.name, b.name)          # different