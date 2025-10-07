import math  # For square root calculations

# Define the upper limit — find all prime numbers below two million
upper_limit = 2_000_000

# Initialize a Boolean list where each index represents if the number is prime
is_prime = [True] * (upper_limit + 1)

# 0 and 1 are not prime numbers
is_prime[0] = False
is_prime[1] = False

# Sieve of Eratosthenes: eliminate multiples of each prime
for candidate in range(2, int(math.sqrt(upper_limit)) + 1):
    if is_prime[candidate]:
        # Mark all multiples of the current prime as non-prime
        for multiple in range(candidate * candidate, upper_limit + 1, candidate):
            is_prime[multiple] = False

# Extract all numbers marked as prime
prime_numbers = [number for number, prime_flag in enumerate(is_prime) if prime_flag]

# Compute and display the sum of all primes below the limit
sum_of_primes = sum(prime_numbers)
print(sum_of_primes)