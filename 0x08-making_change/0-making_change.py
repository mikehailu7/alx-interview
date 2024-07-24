#!/usr/bin/python3
"""Author: MikiasHailu"""


def makeChange(coins, total):
    """This function is called makechange"""
    if total <= 0:
        return 0
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count = count + 1
            elif value < newList[index]:
                index = index + 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
