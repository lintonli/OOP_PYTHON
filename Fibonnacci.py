def fibonacci(n):
    if n <= 0:
        return []
    fib_sequence = [1,2]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]

print(fibonacci(10))