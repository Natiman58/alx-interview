#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]   # [ 0b11100101 0b1000001 0b1111111 0b100000000 ]
print(validUTF8(data))

data = [120, 120, 127, 120, 120]
print(validUTF8(data))    # '0b1111000' '0b1111000' '0b1111000' '0b1111000' '0b1111000'