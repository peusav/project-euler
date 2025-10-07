import math  # Import the math module for mathematical functions (like square root)

# Initialize the variable to store the largest prime factor found
largest_prime_factor = 0

# The number we want to factorize
n = 600851475143

# Loop through all possible factors from 2 up to the square root of n
# (No need to check beyond the square root because any larger factor would have a corresponding smaller one)
for i in range(2, int(math.sqrt(n) + 1)):

    # While 'i' divides 'n' evenly, it means 'i' is a prime factor
    while n % i == 0:
        largest_prime_factor = i  # Update the largest prime factor found so far
        n = n / i  # Divide n by i to reduce it (removing this factor from n)

# After the loop, the last recorded value of 'largest_prime_factor' is the largest prime factor of the original n
print(largest_prime_factor)