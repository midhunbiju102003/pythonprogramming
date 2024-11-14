
class Rectangle:
    def __init__(self, length, breadth):
        # Initialize the attributes of the rectangle
        self.length = length
        self.breadth = breadth

    def area(self):
        # Calculate the area of the rectangle
        return self.length * self.breadth

# Input from the user
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Create a rectangle object with the user inputs
rect = Rectangle(length, breadth)

# Print the area of the rectangle
print(f"Area of the rectangle: {rect.area()}")
