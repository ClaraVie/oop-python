# Inheritance = Allows a class to inherit attributes from another class
#               Helps with code reusability and extensibility
#               class Chlid(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        self.sleep = print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# print(dog.name)
# print(dog.isAlive)
# dog.eat()
# dog.sleep()

dog.speak()
cat.speak()
mouse.speak()