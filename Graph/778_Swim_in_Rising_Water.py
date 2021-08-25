#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:54:51 2021

@author: jeff
"""

"""
Key Idea:
    Use binary search to find T and us dfs to find if it is possible
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visited = set()
        n = len(grid)
        
        def dfsPossible(i, j, T):
            if (i, j) == (n-1, n-1) and grid[i][j] <= T:
                return True
            if 0 <= i < n and 0 <= j < n and grid[i][j] <= T and (i, j) not in visited:
                visited.add((i, j))
                res = dfsPossible(i+1, j, T) or dfsPossible(i, j+1, T) or dfsPossible(i-1, j, T) or dfsPossible(i, j-1, T)
                return res
            return False
            
        low = grid[0][0]
        high = n*n
        while high > low:
            mid = (high + low) // 2
            visited.clear()
            if not dfsPossible(0, 0, mid):
                low = mid + 1
            else:
                high = mid
                
        return low