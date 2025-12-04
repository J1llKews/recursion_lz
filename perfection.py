def sum_of_divisors(n, i=1):
    if i == n:
        return 0
    if n % i == 0:
        return i + sum_of_divisors(n, i + 1)
    else:
        return sum_of_divisors(n, i + 1)

def is_perfect(n):
    return sum_of_divisors(n) == n


def main():
    for num in range(1, 10001):
        if is_perfect(num):
            print(f"{num} — совершенное число")

if __name__ == "__main__":
    main()