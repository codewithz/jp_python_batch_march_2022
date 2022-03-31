class Animal:
    def eat(self):
        print("Eat")

# -----------------------------------------------------
# Animal : Parent or a Base Class
# Mammal , Fish : Child or a Dervied Class

#  class Child(Parent):


# -----------------------------------------------------
class Mammal(Animal):
    def walk(self):
        print("Walk")

#-------------------------------------------------------
class Fish(Animal):
    def swim(self):
        print("Swim")

#  ---------- DRY -- Don't Repeat Yourself -----------------

m=Mammal()
m.eat()
m.walk()

f=Fish()
f.eat()
f.swim()