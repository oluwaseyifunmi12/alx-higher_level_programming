#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary)

    for key in dict:
        print(f"{key}: {a_dictionary[key]}")
