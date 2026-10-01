# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

from car import Car

car1 = Car("Mustang", 1980, "red", False)
car2 = Car("Corvette", 1978, "blue", True)
car3 = Car("Charger", 2011, "yellow", True)

print(f"Total de objetos: {Car.num_cars}")
print(f"Ano de aquisição: {Car.acquisition_year}")