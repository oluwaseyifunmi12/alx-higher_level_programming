#!/usr/bin/python3

def no_c(my_string):
    rm = {'c', 'C'}
    res = ''.join(char for char in my_string if char not in rm)
    return res
