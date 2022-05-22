#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    A = (1, 2, 3)
    B = (4, 5, 6)
    C = A + B
    print(C)

    D = (3, "abc") + (-7.22, ['a', 5])
    print(D)

    A = ('a', 'aa', 'aaa')
    B = A + (1, 2) + (True, False)
    print(B)

    A = (1, 2, 3) * 3
    print(A)

    B = ("ab", ["1", "12"]) * 2
    print(B)
