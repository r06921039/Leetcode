#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 18:12:10 2021

@author: jeff
"""

"""
Key Idea:
    Use dfs to iterate through all possibility
    Use (r+x, c+y, step) as key to memorize
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        memo = {}
        
        def dfs(r, c, step, prob):
            if 0 <= r < n and 0 <= c < n and step < k:
                total = 0
                for x, y in [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]:
                    if (r+x, c+y, step) not in memo:
                        memo[(r+x, c+y, step)] = dfs(r+x, c+y, step+1, prob/8)
                    total += memo[(r+x, c+y, step)]
                return total
            else:
                if 0 <= r < n and 0 <= c < n:
                    return prob
                else:
                    return 0
        return dfs(row, column, 0, 1)