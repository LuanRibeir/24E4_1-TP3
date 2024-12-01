# 8. Demonstre como otimizar uma função recursiva para contornar esses desafios.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))


def fibonacciMemo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
    return memo[n]

print(fibonacciMemo(10))

