#!/usr/bin/env python3
def fibonacci_sequence(n):
    fibonacci = []
    our_range = range(n)
    for y in our_range:
        if y < 2:
            fibonacci.append(y)
        else:
            x = fibonacci[y - 1] + fibonacci[y - 2]
            fibonacci.append(x)
    return fibonacci
