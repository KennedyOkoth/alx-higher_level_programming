#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a)):
        results = tuple(tuple_a(i) + tuple_b(i))
        return results
