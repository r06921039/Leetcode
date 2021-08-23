#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:47:35 2021

@author: jeff
"""

"""
Key Idea:
    Use DFS
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(i):
            if i < 0 or i >= len(arr) or i in visited:
                return False
            visited.add(i)
            if arr[i] == 0:
                return True
            return dfs(arr[i] + i) or dfs(i - arr[i])
        
        return dfs(start)