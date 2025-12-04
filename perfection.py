def sum_of_divisors(n, i=1):
    if i == n:
        return 0
    if n % i == 0:
        return i + sum_of_divisors(n, i + 1)
    else:
        return sum_of_divisors(n, i + 1)


def is_perfect(n):
    return sum_of_divisors(n) == n