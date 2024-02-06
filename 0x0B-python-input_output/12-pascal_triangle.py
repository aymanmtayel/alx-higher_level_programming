#!/usr/bin/python3
"""PASCAL TRIANGLE module"""


def pascal_triangle(n):
    """function to return a pascal triangle of n"""
    if n <= 0:
        return []

    lista = [[1]]
    while len(lista) != n:
        lista2 = lista[-1]
        curr = [1]
        for i in range(len(lista2) - 1):
            curr.append(lista2[i] + lista2[i + 1])
        curr.append(1)
        lista.append(curr)
    return lista
