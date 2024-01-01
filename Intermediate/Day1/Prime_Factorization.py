def prime_factors(n):
    """
    Find the prime factors of a given number.

    Parameters:
    - n (int): Input number

    Returns:
    list: List of prime factors.
    """
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


# Example usage:
num = int(input("Enter a number to find its prime factors: "))
result = prime_factors(num)
print(f"Prime factors of {num}: {result}")
