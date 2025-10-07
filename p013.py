# Loop through all possible values of 'a' from 1 to 999
for a in range(1, 1000):
    
    # For each 'a', loop through all possible values of 'b' from 1 to 999
    for b in range(1, 1000):
        
        # Check if (a, b, c) form a Pythagorean triplet such that a + b + c = 1000
        # Using the condition: a² + b² = c², where c = 1000 - a - b
        if (a**2 + b**2) == (1000 - a - b)**2:
            
            # If the condition is true, compute and print the product a * b * c
            print(a * b * (1000 - a - b))
            
            # Exit the program immediately after finding the correct triplet
            exit()