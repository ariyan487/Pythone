import math

# Function to solve quadratic equations
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Determine the nature of roots based on the discriminant
    if D > 0:
        # Two real and distinct roots
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"The roots are: {x1:.2f} and {x2:.2f}"
    elif D == 0:
        # One real root
        x = -b / (2*a)
        return f"The root is: {x:.2f}"
    else:
        # Complex roots
        return "Roots are imaginary"

# Input values
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation and print the result
print(solve_quadratic(a, b, c))







