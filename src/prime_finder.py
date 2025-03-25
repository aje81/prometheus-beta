def find_primes_in_range(a: int, b: int) -> list[int]:
    """
    Find all prime numbers within a given range (inclusive).

    Args:
        a (int): Lower bound of the range
        b (int): Upper bound of the range

    Returns:
        list[int]: A sorted list of prime numbers within the range

    Raises:
        ValueError: If input bounds are invalid (a > b or negative numbers)
    """
    # Validate input range
    if a > b:
        raise ValueError("Lower bound must be less than or equal to upper bound")
    if a < 0 or b < 0:
        raise ValueError("Both bounds must be non-negative integers")

    # Special case handling for small ranges
    if b < 2:
        return []

    # Use the Sieve of Eratosthenes algorithm
    # Create a boolean array "is_prime[0..b]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (b + 1)
    is_prime[0] = is_prime[1] = False

    # Use Sieve of Eratosthenes to mark non-primes 
    for i in range(2, int(b**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, b+1, i):
                is_prime[j] = False

    # Collect primes in the specified range
    return [num for num in range(max(2, a), b+1) if is_prime[num]]