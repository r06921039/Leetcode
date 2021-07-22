#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 22:38:48 2021

@author: jeff
"""

"""

Key Idea:
    Use BFS to make sure it is the minimum path.

"""



import collections

def Solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1
    
    nrow, ncol = len(m), len(m[0])
    queue = collections.deque([((0,0), 0)])
    m[0][0] = "D"
    while queue:
        (x, y), step = queue.popleft()
        for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if m[x+dx][y+dy] == "X":
                    return step + 1
                elif m[x+dx][y+dy] == "O":
                    m[x+dx][y+dy] = "D"
                    queue.append(((x+dx, y+dy), step + 1))

m = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(Solution(m))