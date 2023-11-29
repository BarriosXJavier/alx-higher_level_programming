#!/usr/bin/python3
for j in range(9):
    for k in range(j + 1, 10):
        if j * 10 + k < 89:
            print("{:d}{:d}".format(j, k), end=", ")
print("{:d}".format(89))
