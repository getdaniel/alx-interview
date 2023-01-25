#!/usr/bin/python3
""" UTF-8 Validation."""


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding.
    """
    try:
        decoded_data = bytes(data).decode('utf-8')
        return True
    except:
        return False
