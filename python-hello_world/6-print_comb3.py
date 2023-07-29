#!/usr/bin/python3
def print_combinations():
    for i in range(10):
        for j in range(i+1, 10):
            print(f"{:d}{:d}".format(i, j))

print_combinations()
