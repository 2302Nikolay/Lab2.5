#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    # A = tuple(map(int, input().split()))

    A = (9, 2, 5, 3, 6, 10, 5, 6, 0, 13, 2)

    ind = 0
    # Нахожу последнюю тройку элементов, в которой средний больше соседних
    for i in range(1, len(A)):
        if (A[i - 1] < A[i]) and (A[i + 1] < A[i]):
            ind = i

    # Вывожу в строку все элементы, предшествующие этой тройки
    print([A[i] for i in range(0, ind-1)])
