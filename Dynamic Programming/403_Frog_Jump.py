#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:37:01 2021

@author: jeff
"""

"""
Key Idea:
    Use a 2D array to keep record
    dp[i][j] = True means from stone i its next jump with j units is available
    Use 2 for loop, for every stone i, check stone j where j < i  if theres dp[j][dist] True
    If Yes and i == n-1 then return True
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False for _ in range(n+1)] for _ in range(n)]
        dp[0][1] = True
        
        for i in range(1, n):
            for j in range(i):
                dist = stones[i] - stones[j]
                if dist < 0 or dist >= n+1 or not dp[j][dist]:
                    continue
                else:
                    if dist-1 >= 0:
                        dp[i][dist-1] = True
                    if dist+1 < n+1:
                        dp[i][dist+1] = True
                    dp[i][dist] = True
                    if i == n-1:
                        return True
                    
        return False