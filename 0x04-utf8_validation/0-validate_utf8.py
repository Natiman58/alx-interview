#!/usr/bin/python3
"""
    This is a simple script to check UTF-8 validation
"""
# For 1-byte character, the first bit is 0, followed by it's unicode
# For n-byte character, the first n-bits are all 1, the n+1 bit is 0
# followed by n-1 bytes with most significant 2 bits bing 10.
# Each integer represents only 1 byte of data
# and handle only the 8 least significant bits of each integer
# 1 integer = 1 byte = 8 bits
# Eg: 65 = 0b 0100 0001

def validUTF8(data):
    """
    checks if data is valid UTF-8
    return the number of byte
    """
    n_bytes = 0

    mask1 = 1 << 7

    mask2 = 1 << 6
    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
