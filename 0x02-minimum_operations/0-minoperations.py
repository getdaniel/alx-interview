#!/usr/bin/python3
""" Defines minOperations."""


def minOperations(n):
    """ Returns an integer.
        if n is imposible to achieve, return 0.
    """
    if not isinstance(n, int):
        return 0
    numOperations = 0
    clipboard = 1
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            numOperations += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            numOperations += 2
        elif clipboard > 0:
            done += clipboard
            numOperations += 1

    return numOperations
