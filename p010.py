# Calculate the sum of the squares of the first 100 natural numbers
# Example: 1² + 2² + 3² + ... + 100²
sum_square = sum([n**2 for n in range(1, 101)])

# Calculate the square of the sum of the first 100 natural numbers
# Example: (1 + 2 + 3 + ... + 100)²
square_sum = (sum([n for n in range(1, 101)]))**2

# Print the difference between the square of the sum and the sum of the squares
print(square_sum - sum_square)
