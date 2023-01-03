#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False."""
    n = len(boxes)
    opened_boxes = set([0])
    unoppened_boxes = set(boxes[0]).difference(set([0]))

    while len(unoppened_boxes) > 0:
        box_key = unoppened_boxes.pop()

        if not box_key or box_key >= n or box_key < 0:
            continue
        if box_key not in opened_boxes:
            unoppened_boxes = unoppened_boxes.union(boxes[box_key])
            opened_boxes.add(box_key)

    return n == len(opened_boxes)
