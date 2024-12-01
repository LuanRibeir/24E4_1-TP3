# 4. Utilizando os algoritmos recursivos de Fibonacci e Fatorial, 
# identifique e explique o Big O de cada um.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2^n)

print(fibonacci(10))

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

# O(n)

print(fatorial(5))