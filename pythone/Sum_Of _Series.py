def sum_of_natural_numbers(n):
    # Initialize sum to 0 or i to 1
    total_sum = 0
    i = 1

    # Repeat until i <= n
    while i <= n:
        total_sum += i   # Sum = Sum + i
        i+=1             # i = i + 1

    return total_sum

# Take input n
n = int(input("Enter the value of n: "))

# Calculate the sum
result = sum_of_natural_numbers(n)

# Print the sum
print("The sum of the series is:", result)


# For n^2 // i = i + 2

def sum_of_odd_squares(n):
    # Initialize sum to 0 and i to 1
    total_sum = 0
    i = 1

    # Repeat until i <= n
    while i <= n:
        total_sum += i**2  # Sum = Sum + i^2
        i += 2             # i = i + 2

    return total_sum

# Take input n
n = int(input("Enter the value of n: "))

# Calculate the sum
result = sum_of_odd_squares(n)

# Print the sum
print("The sum of the series is:", result)