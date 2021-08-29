#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 23:52:58 2021

@author: jeff
"""

"""
Key Idea:
    Use Dfs + Binary search 
    Same as swim in rising water
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        self.visited = set()
        self.visited.add((0,0))
        nrow = len(heights)
        ncol = len(heights[0])
        
        def dfs(i, j, limit):
            if (i, j) == (nrow-1, ncol-1):
                return True
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= i+di < nrow and 0 <= j+dj < ncol and abs(heights[i][j] - heights[i+di][j+dj]) <= limit and (i+di, j+dj) not in self.visited:
                    self.visited.add((i+di, j+dj))
                    if dfs(i+di, j+dj, limit):
                        return True
            
            return False
        
        low, high = 0, max(list(map(max, heights)))
        
        while low < high:
            mid = (low + high) // 2
            self.visited.clear()
            if not dfs(0, 0, mid):
                low = mid + 1
            else:
                high = mid
                
        return low
                    