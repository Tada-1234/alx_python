#!/usr/bin/python3
for n in range(0, 100):
    print("{:02d}".format(n), end="")
    if n < 99:
        print(end = ", ")
    else:
        print(end = " ")
