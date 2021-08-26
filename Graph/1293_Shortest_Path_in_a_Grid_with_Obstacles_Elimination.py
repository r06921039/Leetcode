#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:14:57 2021

@author: jeff
"""

"""
Key Idea:
    Add state: (i, j, quota)
    Store state in visited
    Remember to check quota - grid[i+di][j+dj]
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()
        if k >= nrow + ncol - 2:
            return nrow + ncol - 2
        
        self.steps = 0
        queue = collections.deque([(0, 0, k)])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j, quota = queue.popleft()
                if (i,j) == (nrow-1,ncol-1):
                    return self.steps
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0 <= i+di < nrow and 0 <= j+dj < ncol and (i+di, j+dj, quota-grid[i+di][j+dj]) not in visited and quota-grid[i+di][j+dj] >= 0:
                        visited.add((i+di, j+dj, quota-grid[i+di][j+dj]))
                        queue.append((i+di, j+dj, quota-grid[i+di][j+dj]))
            self.steps += 1
                        
        
        return -1