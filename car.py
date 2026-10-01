class Car:

    num_cars = 0 # class variable
    acquisition_year = 2021

    def __init__(self, model, year, color, for_sale): #constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_cars += 1

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model} {self.for_sale}")