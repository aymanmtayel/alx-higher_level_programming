#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ae1 = tuple_a[0] if len(tuple_a) > 0 else 0
    ae2 = tuple_a[1] if len(tuple_a) > 1 else 0
    be1 = tuple_b[0] if len(tuple_b) > 0 else 0
    be2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (ae1 + be1, ae2 + be2)
