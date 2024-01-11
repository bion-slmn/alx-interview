#!/usr/bin/python3
''' defines canUNloack boxes'''


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    # Iterate over the keys (box indices) starting from the second box
    for key in range(1, len(boxes)):
        flag = False  # Initialize a flag to track if a key can unlock any box

    # Iterate over all boxes
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break

        if not flag:
            return False

    # If all keys can unlock at least one box, return True
    return True
