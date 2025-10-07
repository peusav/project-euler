import math  # Import the math module for square root calculations

# Initialize the list with the first few known prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19]

# Start checking for primes beginning from 20
n = 20

# Continue searching until we find the 10,001st prime number
while len(primes) < 10001:
    
    # Create a list of primes to test as possible divisors of n.
    # Only use primes up to the square root of n, since no larger factor is needed.
    primes_to_test = [test_fat for test_fat in primes if test_fat in range(2, int(math.sqrt(n) + 1))]

    # Test whether n is divisible by any of the primes_to_test.
    # This list comprehension produces True if divisible, False otherwise.
    test = [n % prime == 0 for prime in primes_to_test]

    # If no divisors were found (sum(test) == 0), then n is prime.
    if sum(test) == 0:
        primes.append(n)  # Add n to the list of primes
        print("{} prime numbers found".format(len(primes)))  # Progress indicator
    
    # Increment n to test the next number
    n = n + 1

# After finding 10,001 primes, print the last (i.e., the 10,001st prime number)
print(primes[-1])