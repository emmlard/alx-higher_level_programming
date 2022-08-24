#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return("{} is lower".format(c))
    else:
        return("{} is upper".format(c))
