# Initialize a variable to store the total sum of all multiples of 3 or 5
sum_of_all_multiples = 0

# Loop through all numbers from 0 up to (but not including) 1000
for n in range(1000):

    # Check if the number is a multiple of 3 or 5
    if n % 3 == 0 or n % 5 == 0:

        # If it is, add it to the running total
        sum_of_all_multiples = sum_of_all_multiples + n

# Print the final result
print(sum_of_all_multiples)