"""
The function pathReduc() takes a list of directions (ls) as an input and reducts it to contain a path without redundant paths (for example NORTH -> SOUTH)

Sample input: ["NORTH", "SOUTH", "EAST", "WEST"]
Sample output: []
"""
from typing import List

def pathReduc(ls: List[str]) -> List[str]:
    needless_paths = [
        ["NORTH", "SOUTH"],
        ["SOUTH", "NORTH"],
        ["EAST", "WEST"],
        ["WEST", "EAST"],
    ]

    ix = 0
    while ix < len(ls) - 1:
        if ls[ix] == ls[ix + 1]:
            ix += 1
        else:
            if [ls[ix], ls[ix + 1]] in needless_paths:
                ls.pop(ix + 1)
                ls.pop(ix)
                if ix != 0:
                    ix -= 1
            else:
                ix += 1

    return ls
