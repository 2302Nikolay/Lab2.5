#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

if __name__ == '__main__':

    A = tuple(map(int, input().split()))

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    s = sum(a for a in A if abs(a) < 5)
    print(s)
