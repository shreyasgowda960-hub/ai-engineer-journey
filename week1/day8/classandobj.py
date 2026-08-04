class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog=Dog("Ruff", 3)            
print(my_dog.name)
print(my_dog.age)
my_dog.bark()

golden_ret=Dog("Bruno", 5)
print(golden_ret.name)

