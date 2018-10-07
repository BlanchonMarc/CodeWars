def count_odd_pentaFib(n):
    if n < 5:
        return 1

    Fib = [1, 1, 2, 4]
    for i in range(4, n):
        Fib.append(
            Fib[i - 5] + Fib[i - 4] + Fib[i - 3] + Fib[i - 2] + Fib[i - 1])

    FibSet = set(Fib)

    return sum([(value & 1) == 1 for value in FibSet])
