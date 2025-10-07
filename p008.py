# Define a recursive function to check if a given string 'k' is a palindrome
def is_palindrome(k):
    
    # Base case 1: A single-character string is always a palindrome
    if len(k) == 1:
        return True
    
    # Base case 2: For a two-character string, check if both characters are the same
    elif len(k) == 2:
        return k[0] == k[1]
    
    # Recursive case: 
    # A string is a palindrome if its first and last characters are equal 
    # AND the substring in between is also a palindrome
    else:
        return k[0] == k[-1] and is_palindrome(k[1:-1])


# Initialize the variable that will store the largest palindrome found
largest_palindrome = 0

# Loop through all 3-digit numbers (from 100 to 999)
for i in range(100, 1000):

    # Inner loop to multiply 'i' by every 3-digit number 'j'
    for j in range(100, 1000):

        # Calculate the product of the two numbers
        product = i * j
        
        # Convert the product to a string and check if it’s a palindrome
        if is_palindrome(str(product)):

            # If it’s a palindrome and larger than any found before, update the record
            if largest_palindrome <= product:
                largest_palindrome = product

# After checking all combinations, print the largest palindrome found
print(largest_palindrome)