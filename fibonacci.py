#打印斐波那契数列前10项
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a+b
    return fib_sequence

n = 10
print(fibonacci(n))
