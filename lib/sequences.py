def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    if length == 1:
        print([0])
        return
    if length == 2:
        print([0, 1])
        return

    fib = [0, 1]
    while len(fib) < length:
        next_value = fib[-1] + fib[-2]
        fib.append(next_value)

    print(fib)
