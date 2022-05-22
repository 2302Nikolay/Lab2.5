#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    A = (0, 1, 2, 3)
    item = A[0:2]
    print(item)

    A = (2.5, ['abcd', True, 3.1415], 8, False, 'z')
    item = A[1:3]
    print(item)

    A = (3, 8, -11, "program")
    B = ("Python", A, True)
    item = B[:3]
    print(item)
    item = B[1:]
    print(item)
