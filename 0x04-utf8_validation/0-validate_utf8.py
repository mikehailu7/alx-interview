#!/usr/bin/python3
# Author: MikiasHailu
"""Utf8 validaiton module"""

def get_leading_set_bits(num):
    """ This funciton will return the latest set bit"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """ This funciton will determine if it have a valid encoding"""
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            '''check the length of the bits'''
            if bits_count == 0:
                continue
            '''check the length of the bits'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''check the current format'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
