# super() = Function used in a child class to call methods from a parent class
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self) -> None:
        print(f"Circle with an area of {3.14 * self.radius ** 2}cm²")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Square with an area of {self.width ** 2}cm²")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

    def describe(self):
        print(f"Triangle with an area of {self.height * self.width / 2}cm²")
        super().describe()

circle = Circle("red", True, 4)
square = Square("blue", False, 6)
triangle = Triangle("green", True, 4, 7)

# print(square.color)
# print(square.is_filled)
# print(square.width)

# print(triangle.color)
# print(triangle.is_filled)
# print(f"{triangle.height}cm")
# print(f"{triangle.width}cm")

circle.describe()
square.describe()
triangle.describe()