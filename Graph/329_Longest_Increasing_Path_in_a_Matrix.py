#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:29:28 2021

@author: jeff
"""

"""
Key Idea:
    Keep a dictionary to memorize the distance of visited node
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        nrow = len(matrix)
        ncol = len(matrix[0])
        ans = 0
        
        def dfs(i, j, last_val):
            if matrix[i][j] <= last_val:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            dist = 0
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= di+i < nrow and 0 <= dj+j < ncol:
                    dist = max(dist, dfs(di+i, dj+j, matrix[i][j]))
            memo[(i, j)]= dist + 1
            return dist + 1
        
        for i in range(nrow):
            for j in range(ncol):
                ans = max(ans, dfs(i, j, float("-inf")))
                
        return ans