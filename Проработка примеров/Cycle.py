#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    A = ("abc", "abcd", "bcd", "cde")
    for item in A:
        print(item)

    A = (-1, 3, -8, 12, -20)
    i = 0
    k = 0
    while i < len(A):
        if A[i] < 0:
            k = k + 1
    i = i + 1
    print("k = ", k)

    B = [item * 2 for item in A]
    print("A = ", A)
    print("B = ", B)
