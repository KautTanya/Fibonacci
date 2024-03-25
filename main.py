"""Fibonacci"""


def fibonacci(n):
    """Fibonacci"""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, b+a


for i in fibonacci(100):
    print(i)
