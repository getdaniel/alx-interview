#!/usr/bin/python3
""" UTF-8 Validation."""


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        byte_count = 0
        if (data[i] & 128) == 0:
            byte_count = 1
        elif (data[i] & 224) == 192:
            byte_count = 2
        elif (data[i] & 240) == 224:
            byte_count = 3
        elif (data[i] & 248) == 240:
            byte_count = 4
        else:
            return False

        for j in range(1, byte_count):
            if i+j >= len(data) or (data[i+j] & 192) != 128:
                return False
        i += byte_count
    return True
