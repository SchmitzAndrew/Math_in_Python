def fibonacci(n):  # generate fibonacci numbers recursively
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(f):
    if f == 1:
        return 1
    else:
        return (f * factorial(f-1))
