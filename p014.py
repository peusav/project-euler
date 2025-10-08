def collatz_sequence_length(n, cache):
    """
    Calculates the length (number of terms) of the Collatz sequence for a given number n.

    The Collatz sequence is defined as follows:
        - If n is even, the next term is n / 2
        - If n is odd, the next term is 3n + 1
        - The sequence ends when n = 1

    This algorithm uses memoization (caching) to avoid recalculating sequences
    that have already been computed.

    Parameters:
    -----------
    n : int
        Starting number for which the Collatz sequence length will be calculated.
    cache : dict
        Dictionary that stores lengths of previously computed sequences.
        The key is the number, and the value is the length of its sequence.

    Returns:
    --------
    int
        The total length of the Collatz sequence starting from n.
    """
    # Check if the value has already been computed and stored in cache
    if n in cache:
        return cache[n]

    # If n is even, apply n / 2
    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2, cache)
    # If n is odd, apply 3n + 1
    else:
        length = 1 + collatz_sequence_length(3 * n + 1, cache)

    # Store the computed result in cache for future reuse
    cache[n] = length
    return length


# Initialize the cache with the base case of the Collatz sequence (n = 1)
cache = {1: 1}

# Variables to keep track of the longest sequence and its corresponding number
longest_chain = 0
number_with_longest = 1

# Main loop: test every number from 1 up to 1,000,000
for n in range(1, 1_000_000):
    # Compute the sequence length for the current number
    length = collatz_sequence_length(n, cache)

    # Update the record if a longer sequence is found
    if length > longest_chain:
        longest_chain = length
        number_with_longest = n

# Display the final result
print(f"The number with the longest Collatz sequence is {number_with_longest} with {longest_chain} terms.")