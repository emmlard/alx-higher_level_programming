#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for item, a in sorted(a_dictionary.items()):
        print("{}: {}".format(item, a))
