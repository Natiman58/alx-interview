#!/usr/bin/python3
"""
    A method that checks if all the boxes can be unlocked.
"""
def canUnlockAll(boxes):
    keys = [0]
    """ loop through boxes array and
        find the index of each element(inner boxes)
    """
    for index, item in enumerate(boxes):
        if not item:
            continue
        for key in item:
            """ loop through each key in item(inner box)
                and append the key to keys array
            """
            if key < len(boxes) and key not in keys and key != index:
                keys.append(key)
    """ if the number of keys is equal to number of inner boxes
        return True; else False
    """
    if len(keys) == len(boxes):
        return True
    return False
