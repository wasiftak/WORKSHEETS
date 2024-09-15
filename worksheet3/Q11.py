import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print(f"Area: {circle.area()}")          # Output: Area of the circle
print(f"Perimeter: {circle.perimeter()}") # Output: Perimeter of the circle
