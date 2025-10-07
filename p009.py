import math

# List of numbers from 1 to 20 (the range we want the LCM for)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Dictionary of prime numbers up to 20
# Keys = prime numbers, values = initial exponent (starts at 1)
primes_fat = {
    2: 1,
    3: 1,
    5: 1,
    7: 1,
    11: 1,
    13: 1,
    17: 1,
    19: 1
}

# For each number from 1 to 20
for n in numbers:
    # Check divisibility by each prime
    for prime in primes_fat.keys():
        i = 0  # exponent counter for this prime
        # While the number is divisible by the prime
        while n % prime == 0:
            i = i + 1  # increase exponent count
            # If the exponent in the dictionary is smaller, update it
            if primes_fat[prime] < i:
                primes_fat[prime] = i
            # Divide n by prime to continue factoring
            n = n / prime

# Multiply each prime raised to its maximum exponent found
smallestPositive = math.prod([p ** exp for p, exp in primes_fat.items()])

# Print the final result (LCM of numbers 1 to 20)
print(smallestPositive)