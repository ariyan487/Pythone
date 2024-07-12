#Finding the smallest number out of three numbers
def find_smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
# Define the numbers
a,b,c = 100,200,300
# Find and print the smallest number
print("The smallest number is:", find_smallest(a,b,c))