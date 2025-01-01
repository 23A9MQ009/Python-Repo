def nearest_fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] == n:
        return n
    diff1 = abs(fib[-1] - n)
    diff2 = abs(fib[-2] - n)
    if diff1 == diff2:
        return fib[-2], fib[-1]
    elif diff1 < diff2:
        return fib[-1]
    else:
        return fib[-2]
n = int(input())
result = nearest_fibonacci(n)
if isinstance(result, tuple):
    print(result[0], result[1])
else:
    print(result)
