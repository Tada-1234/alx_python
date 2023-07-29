#!/usr/bin/python3
def print_combinations():
    for i in range(10):
        for j in range(i+1, 10):
            if i < 8:
                print("{:d}{:d}".format(i, j), end = ", ")
            else:
                print("{:d}{:d}".format(i, j), end = " ")

print_combinations()
