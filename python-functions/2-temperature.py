#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    celsius = (5 / 9)*(fahrenheit - 32)
    if celsius < 0:
        celsius = round(celsius, 2)
    return celsius
