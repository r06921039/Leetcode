#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:28:01 2021

@author: jeff
"""

"""
Key Idea:
    Use BFS
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        self.length = 1
        queue = collections.deque([(0,0)])
        visited = set()
        n = len(grid)
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if (i, j) == (n-1, n-1):
                    return self.length
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]:
                    if 0 <= i+di < n and 0 <= j+dj < n and (i+di, j+dj) not in visited and grid[i+di][j+dj] == 0:
                        visited.add((i+di, j+dj))
                        queue.append((i+di, j+dj))
                
            self.length += 1
            
        
            
        return -1