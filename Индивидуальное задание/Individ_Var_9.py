#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    # Картеж с числами для теста работы программы:
    A = (9, 2, 5, 3, 6, 10, 5, 6, 0, 13, 2)
    # A = tuple(map(int, input().split()))

    ind = 0
    # Нахожу последнюю тройку элементов, в которой средний больше соседних
    for n, i in enumerate(A):
        if A[n - 1] < A[n] and A[n + 1] < A[n]:
            ind = n

    # Вывожу в строку все элементы, предшествующие этой тройки
    print([A[i] for i in range(0, ind-1)])
