# Function to count how many divisors a number 'n' has
def count_divisors(n):
    count = 0
    sqrt_n = int(n ** 0.5)  # Calculate the integer square root of n
    
    # Loop through possible divisors from 1 up to √n
    for d in range(1, sqrt_n + 1):
        if n % d == 0:  # If d divides n evenly
            count += 2   # Count both d and n/d as divisors
    
    # If n is a perfect square, we counted its square root twice — fix that
    if sqrt_n * sqrt_n == n:
        count -= 1
    
    return count


# Initialize a counter for generating triangle numbers
i = 1

# Infinite loop to find the first triangle number with more than 500 divisors
while True:
    # Calculate the i-th triangle number using the formula: n = i * (i + 1) / 2
    triangle_number = i * (i + 1) // 2

    # Count how many divisors this triangle number has
    divisors = count_divisors(triangle_number)

    # Check if this triangle number has more than 500 divisors
    if divisors > 500:
        print("✅ Number:", triangle_number)
        print("🔢 Divisors:", divisors)
        break  # Stop once the first such number is found

    # Increment i to generate the next triangle number
    i += 1
