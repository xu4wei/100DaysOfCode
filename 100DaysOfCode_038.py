def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series


n = 10
fibonacci_sequence = fibonacci(n)
print(f"The first {n} terms of the Fibonacci sequence are: {fibonacci_sequence}")