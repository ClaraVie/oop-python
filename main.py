# # Duck typing = Another way to achieve polymorphism besides Inheritance
#                 Object msut have minimum necessary attributes/methods
#                 "If it look like a duck and quacks like a duck, it mus be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car(Animal):
    alive = False

    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)