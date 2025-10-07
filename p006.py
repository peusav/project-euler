# Base case: initialize the first two terms of the Fibonacci sequence
a = 1
b = 2

# Store the first two terms in a list (not essential for the logic, just illustrative)
terms = [a, b]

# Variable to hold the current Fibonacci term
n = 0  

# Initialize the sum with 'b' since 2 is the first even Fibonacci number
sum_even_terms = b  

# Continue generating Fibonacci terms until the next term exceeds 4 million
while n < 4000000:
    
    # Generate the next Fibonacci term
    n = a + b

    # If the term is even, add it to the running total
    if n % 2 == 0:
        sum_even_terms = sum_even_terms + n
    
    # Update variables to move forward in the sequence
    a = b
    b = n

# Print the total sum of even Fibonacci numbers below 4 million
print(sum_even_terms)