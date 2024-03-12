#!/usr/bin/python3
# Author: mikiasHailu
"""Lockboxes"""


def canUnlockAll(boxes):
    """this funciton will open all the boxes"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = k in boxes[i] and k != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
