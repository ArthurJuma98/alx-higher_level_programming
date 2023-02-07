#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns the number of characters"""


def write_file(filename=""):
    with open(filename, "r") as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
