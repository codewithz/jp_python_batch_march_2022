class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee,Person):
    pass


m=Manager()
m.greet()

# ------------------------------------------------------------

class Flyer:
    def fly(self):
        print("Fly")

class Swimmer:
    def swim(self):
        print("Swim")


class FlyingFish(Flyer,Swimmer):
    pass

f=FlyingFish()
f.swim()
f.fly()