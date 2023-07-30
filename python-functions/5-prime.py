#!/usr/bin/env python3
def is_prime(number):
    non_negative = (number * number) ** 0.5
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        square_root = int(non_negative ** 0.5) + 1
        for n in range(2, square_root):
            if (number % n) == 0:
                return False
        return True
