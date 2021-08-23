def count_divisors(n):
    if n == 1: return 1
    divisors = 2
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            divisors += 1 if i ** 2 == n else 2
    return divisors

def first_fibonacci_thousand_divisors():
    before, current = 1, 1
    while count_divisors(current) < 1000:
        temp = current
        current += before
        before = temp
    return current

def main():
    print("El primer número de fibonacci con más de mil divisores:", first_fibonacci_thousand_divisors())


if __name__ == "__main__":
    main()

