import math

# Taking user inputs
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Checking if triangle formation is possible
if (a + b > c) and (b + c > a) and (c + a > b):
    # Calculating the semi-perimeter
    s = (a + b + c) / 2
    # Calculating the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Triangular formation is not possible") 











