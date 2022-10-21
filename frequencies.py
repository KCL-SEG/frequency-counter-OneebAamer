"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        frequencies[str(i)] = frequencies.get(str(i),0) + 1;
    return frequencies