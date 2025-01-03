def sum(n):
    if n <= 0:  # Base case: Stop when n is 0 or less
        return 0
    return n + sum(n - 1)  # Recursive case: Add n to the sum of numbers from (n-1)


print(sum(5))